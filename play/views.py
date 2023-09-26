from rest_framework import viewsets

from .models import User, Song, Playlist, Playlist_song, Album, Artist, Interaction
from .serializers import UserSerializer, ArtistSerializer, AlbumSerializer, PlaylistSerializer, SongSerializer, \
    Playlist_songSerializer, InteractionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class Playlist_songViewSet(viewsets.ModelViewSet):
    queryset = Playlist_song.objects.all()
    serializer_class = Playlist_songSerializer


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
