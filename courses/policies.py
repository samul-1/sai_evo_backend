from rest_access_policy import AccessPolicy
from courses.logic.participations import is_time_up

from courses.logic.privileges import check_privilege

from .models import Event, EventTemplate


class BaseAccessPolicy(AccessPolicy):
    def has_teacher_privileges(self, request, view, action, privilege):
        from courses.models import Course
        from courses.views import CourseViewSet

        course_pk = (
            view.kwargs.get("pk")
            if isinstance(view, CourseViewSet)
            else view.kwargs.get("course_pk")  # nested view
        )

        try:
            course = Course.objects.get(pk=course_pk)
        except ValueError:
            return False

        return check_privilege(request.user, course, privilege)


class CoursePolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["list", "unstarted_practice_events"],
            "principal": ["authenticated"],
            "effect": "allow",
        },
        {
            "action": ["set_permissions"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:manage_permissions",
        },
        {
            "action": ["retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_visible_to",
        },
        {
            "action": ["create"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_teacher",
        },
        {
            "action": ["update", "partial_update"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:update_course",
        },
        {
            "action": ["active_users"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:__some__",
        },
    ]

    def is_visible_to(self, request, view, action):
        return True

    def is_teacher(self, request, view, action):
        return request.user.is_teacher


class CourseRolePolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:manage_permissions",
        },
    ]


class EventPolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_course_visible_to",
        },
        {
            "action": ["create", "update", "partial_update"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "is_self_service_practice or has_teacher_privileges:manage_events",
        },
        {
            "action": ["instances"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "has_teacher_privileges:manage_events",
        },
        {
            "action": ["retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "is_event_visible_to",
        },
    ]

    def is_self_service_practice(self, request, view, action):
        try:
            return request.data["event_type"] == Event.SELF_SERVICE_PRACTICE
        except Exception:
            return False

    def is_course_visible_to(self, request, view, action):
        return True

    def is_event_visible_to(self, request, view, action):
        # TODO implement
        return True


class EventTemplatePolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "is_related_to_self_service_practice or has_teacher_privileges:manage_events",
        },
    ]

    def is_related_to_self_service_practice(self, request, view, action):
        from courses.views import (
            EventTemplateRuleClauseViewSet,
            EventTemplateRuleViewSet,
        )

        if isinstance(view, EventTemplateRuleViewSet) or isinstance(
            view, EventTemplateRuleClauseViewSet
        ):
            try:
                template = EventTemplate.objects.get(pk=view.kwargs["template_pk"])
            except ValueError:
                return False
        else:
            template = view.get_object()

        return template.event.event_type == Event.SELF_SERVICE_PRACTICE


class TagPolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
        },
    ]


class ExercisePolicy(BaseAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "bulk_get"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:access_exercises",
        },
        {
            "action": [
                "create",
                "update",
                "partial_update",
                "destroy",
                "tags",
                "solution_execution_results",
            ],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:manage_exercises",
        },
    ]


class ExerciseRelatedObjectsPolicy(BaseAccessPolicy):
    # used for models related to Exercise, like ExerciseChoice,
    # ExerciseTestCase, and Exercise itself when used as a sub-exercise
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:access_exercises",
        },
        {
            "action": ["create", "update", "partial_update", "destroy"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition": "has_teacher_privileges:manage_exercises",
        },
    ]


class EventParticipationPolicyMixin:
    def get_participation(self, view):
        from courses.views import (
            EventParticipationSlotViewSet,
            EventParticipationViewSet,
        )

        if isinstance(view, EventParticipationViewSet):
            participation = view.get_object()
        elif isinstance(view, EventParticipationSlotViewSet):
            participation = view.get_object().participation
        else:
            assert False, f"View {view} isn't of correct type"
        return participation

    def is_own_participation(self, request, view, action):
        participation = self.get_participation(view)
        return request.user == participation.user

    def can_update_participation(self, request, view, action):
        from courses.models import Event, EventParticipation

        participation = self.get_participation(view)

        if participation.state == EventParticipation.TURNED_IN:
            return False

        # check that there is time left for the participation
        if is_time_up(participation):
            return False

        event = participation.event

        return event.state == Event.OPEN or (
            event.state == Event.RESTRICTED
            and request.user in event.users_allowed_past_closure.all()
        )


class EventParticipationPolicy(BaseAccessPolicy, EventParticipationPolicyMixin):
    statements = [
        {
            "action": ["list"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "has_teacher_privileges:manage_events\
                or requested_own_participations",
        },
        {
            "action": ["retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "is_own_participation\
                or has_teacher_privileges:assess_participations",
        },
        {
            "action": ["create"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "can_participate\
                or has_teacher_privileges:manage_events",
        },
        {
            "action": ["go_back"],
            "principal": ["authenticated"],
            "effect": "deny",
            "condition_expression": "not can_go_back",
        },
        {
            "action": ["update", "partial_update", "go_forward", "go_back"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "\
                is_own_participation and \
                    (can_update_participation or is_bookmark_request)\
                or has_teacher_privileges:assess_participations",
        },
        {
            "action": ["go_forward", "go_back"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "\
                is_own_participation and can_update_participation\
                        or has_teacher_privileges:assess_participations",
        },
        {
            "action": ["bulk_patch"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "\
                has_teacher_privileges:assess_participations",
        },
        {
            "action": ["go_forward"],
            "principal": ["authenticated"],
            "effect": "deny",
            "condition_expression": "not can_go_forward",
        },
    ]

    def requested_own_participations(self, request, view, action):
        """
        The user has accessed the viewset as a sub-route of courses and hasn't
        specified a user_id in the params, therefore requesting to view their
        own participations only
        """
        return "user_id" not in request.query_params

    def can_participate(self, request, view, action):
        from courses.models import Event

        try:
            event = Event.objects.get(pk=view.kwargs["event_pk"])
        except Event.DoesNotExist:
            return True
        except (ValueError, KeyError):
            return False

        if event.state != Event.OPEN and (
            event.state != Event.RESTRICTED
            or request.user not in event.users_allowed_past_closure.all()
        ):
            return False

        if event.access_rule == Event.ALLOW_ACCESS:
            return request.user.email not in event.access_rule_exceptions
        else:  # default is DENY_ACCESS
            return request.user.email in event.access_rule_exceptions

    def is_bookmark_request(self, request, view, action):
        # users are allowed to update a participation after it's
        # turned in as long as their request only involves updating
        # the `bookmarked` field
        return "bookmarked" in request.data and len(request.data.keys()) == 1

    def can_go_forward(self, request, view, action):
        participation = view.get_object()
        return not participation.is_cursor_last_position

    def can_go_back(self, request, view, action):
        from courses.models import Event

        participation = view.get_object()
        event = participation.event

        return not participation.is_cursor_first_position and event.allow_going_back


class EventParticipationSlotPolicy(BaseAccessPolicy, EventParticipationPolicyMixin):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "is_own_participation\
                or has_teacher_privileges:assess_participations",
        },
        {
            "action": ["update", "partial_update", "run", "attachment"],
            "principal": ["authenticated"],
            "effect": "allow",
            "condition_expression": "\
                is_own_participation and can_update_participation\
                    or has_teacher_privileges:assess_participations",
        },
        {
            "action": ["retrieve", "update", "partial_update"],
            "principal": ["authenticated"],
            "effect": "deny",
            "condition_expression": "\
                not has_teacher_privileges:assess_participations\
                and not is_slot_in_scope",
        },
    ]

    def is_slot_in_scope(self, request, view, action):
        slot = view.get_object()
        return slot.is_in_scope()
