from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    SettingViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    DislikeViewSet,
    InboxViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("inbox", InboxViewSet)
router.register("like", LikeViewSet)
router.register("dislike", DislikeViewSet)
router.register("userphoto", UserPhotoViewSet)
router.register("setting", SettingViewSet)
router.register("profile", ProfileViewSet)
router.register("match", MatchViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
