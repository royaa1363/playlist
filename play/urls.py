from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, ArtistViewSet, AlbumViewSet, SongViewSet, PlaylistViewSet, InteractionViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("artist", ArtistViewSet)
router.register("album", AlbumViewSet)
router.register("song", SongViewSet)
router.register("playlist", PlaylistViewSet)
router.register("interaction", InteractionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
