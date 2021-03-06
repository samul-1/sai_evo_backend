from courses.logic.privileges import ACCESS_EXERCISES, MANAGE_EXERCISES
from courses.models import Course, CourseRole, UserCoursePrivilege
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User

from django.db.models import Prefetch

from . import policies
from .serializers import UserSerializer


class UserViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # .prefetch_related("roles", "privileged_courses")

    permission_classes = [policies.UserPolicy]

    def get_queryset(self):
        qs = super().get_queryset()

        if "course_id" in self.request.query_params:
            qs = qs.prefetch_related(
                Prefetch(
                    "privileged_courses",
                    queryset=UserCoursePrivilege.objects.filter(
                        course_id=self.request.query_params["course_id"]
                    ),
                    to_attr="prefetched_privileged_courses",
                ),
                Prefetch(
                    "roles",
                    queryset=CourseRole.objects.filter(
                        course_id=self.request.query_params["course_id"]
                    ),
                    to_attr="prefetched_course_roles",
                ),
            )

        return qs

    def get_serializer_context(self):
        context = super().get_serializer_context()
        params = context["request"].query_params
        if "course_id" in params:
            course = get_object_or_404(Course, pk=params["course_id"])
            context["course"] = course
        return context

    @action(detail=False, methods=["get"])
    def me(self, request, **kwargs):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def privileges(self, request, **kwargs):
        params = request.query_params
        if "course_id" in params:
            course = get_object_or_404(Course, pk=params["course_id"])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = self.get_object()

        try:
            new_privileges = request.data["course_privileges"]

            course_privileges, _ = UserCoursePrivilege.objects.get_or_create(
                user=user, course=course
            )

            # prevent users from having edit privileges on exercises if they don't have access to exercises
            if (
                MANAGE_EXERCISES in new_privileges
                and ACCESS_EXERCISES not in course_privileges.allow_privileges
            ):
                new_privileges.append(ACCESS_EXERCISES)

            # if someone is granted edit privileges on exercises, gran them access to exercises
            if ACCESS_EXERCISES not in new_privileges:
                new_privileges = [p for p in new_privileges if p != MANAGE_EXERCISES]

            course_privileges.allow_privileges = new_privileges
            course_privileges.save()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user, context=self.get_serializer_context())
        return Response(serializer.data)
