from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MemberProfileViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'member-profiles', MemberProfileViewSet)

urlpatterns =  [
    path('', include(router.urls)),
]

