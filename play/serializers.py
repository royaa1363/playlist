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
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    artist_name = serializers.CharField(source="artist.name")

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['user_id', 'name', 'rules', 'create_at', 'update_at']


class Playlist_songSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    playlist = PlaylistSerializer()

    class Meta:
        model = Playlist_song
        fields = '__all__'


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['playlist_id', 'song_id']
