from django.urls import include, path
from apps.users.urls import router as users_router
from apps.packages.urls import router as packages_router
from apps.schedules.urls import router as schedules_router
from apps.reviews.urls import router as reviews_router
from apps.progress.urls import router as progress_router
from apps.notifications.urls import router as notifications_router
from apps.payments.urls import router as payment_router
from apps.chats.urls import router as chats_router
from rest_framework.routers import DefaultRouter

# Gộp tất cả router
router = DefaultRouter()
router.registry.extend(users_router.registry)
router.registry.extend(packages_router.registry)
router.registry.extend(schedules_router.registry)
router.registry.extend(reviews_router.registry)
router.registry.extend(progress_router.registry)
router.registry.extend(notifications_router.registry)
router.registry.extend(payment_router.registry)
router.registry.extend(chats_router.registry)
urlpatterns = router.urls
