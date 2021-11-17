from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses import policies
from courses.models import (
    Course,
    Event,
    EventParticipation,
    EventTemplate,
    Exercise,
    ExerciseChoice,
    ParticipationAssessmentSlot,
    ParticipationSubmissionSlot,
)

from .serializers import CourseSerializer  # EventParticipationSerializer,
from .serializers import (
    EventSerializer,
    EventTemplateSerializer,
    ExerciseChoiceSerializer,
    ExerciseSerializer,
    ParticipationAssessmentSlotSerializer,
    ParticipationSubmissionSlotSerializer,
    StudentViewEventParticipationSerializer,
    TeacherViewEventParticipationSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [policies.CoursePolicy]

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
        )


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer  # TODO pass show_hidden_fields in context
    queryset = Exercise.objects.all().prefetch_related(
        "tags",
        "choices",
        "testcases",
        "sub_exercises",
    )
    permission_classes = [policies.ExercisePolicy]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(course_id=self.kwargs["course_pk"])
        if self.kwargs.get("exercise_pk") is not None:
            # using the viewset for sub-exercises
            qs = qs.filter(parent_id=self.kwargs["exercise_pk"])

        # TODO only show base exercises unless you're listing the sub-exercises of an exercise
        return qs

    def perform_create(self, serializer):
        serializer.save(
            course_id=self.kwargs["course_pk"],
            parent_id=self.kwargs.get("exercise_pk", None),
        )


class ExerciseChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseChoiceSerializer
    queryset = ExerciseChoice.objects.all()
    # TODO permissions

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(exercise_id=self.kwargs["exercise_pk"])

    def perform_create(self, serializer):
        serializer.save(
            exercise_id=self.kwargs["exercise_pk"],
        )


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [policies.EventPolicy]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_id=self.kwargs["course_pk"])

    def perform_create(self, serializer):
        serializer.save(
            course_id=self.kwargs["course_pk"],
            creator=self.request.user,
        )


class EventTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = EventTemplateSerializer
    queryset = EventTemplate.objects.public()  # TODO make this
    permission_classes = [policies.EventTemplatePolicy]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_id=self.kwargs["course_pk"])

    def perform_create(self, serializer):
        serializer.save(
            course_id=self.kwargs["course_pk"],
            creator=self.request.user,
        )


class EventParticipationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = EventParticipation.objects.all().select_related(
        "assessment",
        "submission",
    )
    permission_classes = [policies.EventParticipationPolicy]

    def get_serializer_class(self):
        return (
            TeacherViewEventParticipationSerializer
            if self.request.user.is_teacher  # TODO properly check permissions (make a check_teacher_privilege in policies.py and use it here)
            else StudentViewEventParticipationSerializer
        )

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_id=self.kwargs["event_pk"])

    def create(self, request, *args, **kwargs):
        # TODO test if the participation is created with the correct event or if you need to put the event in get_or_create explicitly
        participation, _ = self.get_queryset().get_or_create(user=request.user)
        serializer = StudentViewEventParticipationSerializer(participation)
        return Response(serializer.data)


class EventParticipationSlotViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    permission_classes = [policies.EventParticipationSlotPolicy]

    def get_serializer_class(self):
        return (
            ParticipationAssessmentSlotSerializer
            if self.request.user.is_teacher  # TODO properly check permissions (make a check_teacher_privilege in policies.py and use it here)
            else ParticipationSubmissionSlotSerializer
        )

    def get_queryset(self):
        if (
            self.request.user.is_teacher
        ):  # TODO properly check permissions (make a check_teacher_privilege in policies.py and use it here)
            qs = ParticipationAssessmentSlot.objects.all()
            related_kwarg = {
                "assessment__participation": self.kwargs["participation_pk"]
            }
        else:
            qs = ParticipationSubmissionSlot.objects.all()
            related_kwarg = {
                "submission__participation": self.kwargs["participation_pk"]
            }

        return qs.filter(**related_kwarg).prefetch_related("sub_slots")
