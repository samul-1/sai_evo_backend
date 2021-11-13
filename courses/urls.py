from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from courses import views

# `/courses` entry point
router = routers.SimpleRouter()
router.register(
    r"courses",
    views.CourseViewSet,
    basename="courses",
)
course_router = routers.NestedSimpleRouter(
    router,
    r"courses",
    lookup="course",
)

# `/courses/<pk>/exercies` entry point
course_router.register(
    r"exercises",
    views.ExerciseViewSet,
    basename="course-exercises",
)

# `/courses/<pk>/templates` entry point
course_router.register(
    r"templates",
    views.EventTemplateViewSet,
    basename="course-templates",
)

# `/courses/<pk>/events` entry point
course_router.register(
    r"events",
    views.EventViewSet,
    basename="course-events",
)

event_router = routers.NestedSimpleRouter(course_router, r"events", lookup="event")

# `/courses/<pk>/events/<pk>/participations` entry point
event_router.register(
    r"participations",
    views.EventParticipationViewSet,
    basename="event-participations",
)

participation_router = routers.NestedSimpleRouter(
    event_router, r"participations", lookup="participation"
)

# `/courses/<pk>/events/<pk>/participations/<pk>/slots` entry point
participation_router.register(
    r"slots", views.EventParticipationSlotViewSet, basename="participation-slots"
)

slot_router = routers.NestedSimpleRouter(
    participation_router,
    r"slots",
    views.EventParticipationSlotViewSet,
    lookup="slot",
)
slot_router.register(
    r"slots", views.EventParticipationSlotViewSet, basename="slot-slots"
)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(course_router.urls)),
    path("", include(event_router.urls)),
    path("", include(participation_router.urls)),
    path("", include(slot_router.urls)),
]
