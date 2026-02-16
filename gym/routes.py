from rest_framework import routers
from .views import ClaseViewSet, ReservaViewSet, InstructorViewSet

router = routers.DefaultRouter()
router.register('instructores', InstructorViewSet)
router.register('clases', ClaseViewSet)
router.register('reservas', ReservaViewSet)

urlpatterns = router.urls
