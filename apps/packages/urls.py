from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, MemberPackageViewSet

router = DefaultRouter()
router.register(r'packages', PackageViewSet)
router.register(r'member-packages', MemberPackageViewSet)

urlpatterns = router.urls
