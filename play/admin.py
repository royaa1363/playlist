from django.contrib import admin

from .models import User, Artist, Album, Song, Playlist, Playlist_song, Interaction

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Playlist_song)
admin.site.register(Interaction)