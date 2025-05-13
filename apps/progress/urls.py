from rest_framework.routers import DefaultRouter
from .views import ProgressViewSet

router = DefaultRouter()
router.register(r'progress', ProgressViewSet)

urlpatterns = router.urls
