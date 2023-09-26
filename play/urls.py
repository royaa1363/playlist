from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, ArtistViewSet, AlbumViewSet, SongViewSet, PlaylistViewSet, Playlist_songViewSet, \
    InteractionViewSet

router = routers.DefaultRouter()
router.register("User", UserViewSet)
router.register("Artist", ArtistViewSet)
router.register("Album", AlbumViewSet)
router.register("Song", SongViewSet)
router.register("Playlist", PlaylistViewSet)
router.register("Playsong", Playlist_songViewSet)
router.register("Interaction", InteractionViewSet)

urlpatterns = [
    path("", include(router.urls))
]