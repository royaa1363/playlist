from rest_framework import serializers

from .models import User, Artist, Album, Song, Playlist_song, Playlist, Interaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_admin', 'remember_token', 'create_at', 'update_at']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'create_at', 'update_at']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'cover', 'artist_id', 'create_at', 'update_at']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'length', 'track', 'path', 'album_id', 'artist_id', 'create_at', 'update_at']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['user_id', 'name', 'rules', 'create_at', 'update_at']


class Playlist_songSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_song
        fields = ['playlist_id', 'song_id']

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['playlist_id', 'song_id']
