from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, MemberProfileViewSet
from apps.schedules.views import ScheduleViewSet
from apps.packages.views import PackageViewSet, MemberPackageViewSet
from apps.reviews.views import ReviewViewSet
from apps.progress.views import ProgressViewSet
from apps.notifications.views import NotificationViewSet


# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Router setup
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'member-profiles', MemberProfileViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'member-packages', MemberPackageViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'notifications', NotificationViewSet)


# Swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="Gym Management API",
        default_version='v1',
        description="API documentation for the gym management system",
        contact=openapi.Contact(email="nguyenanhcam10@gmail.com"),
        license=openapi.License(name="Nguyễn Anh Cam@2025"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
