from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=256)
    is_admin = models.BooleanField(null=False)
    remember_token = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):
    name = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=256)
    cover = models.CharField(max_length=256, blank=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.artist}'


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=256)
    length = models.FloatField(null=True, default=0)
    track = models.IntegerField(default=0)
    path = models.TextField(null=True, blank=True)
    mtime = models.IntegerField(null=True, default=0)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=256)
    rules = models.TextField(blank=True)
    songs = models.ManyToManyField(Song)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True)
    liked = models.BooleanField(null=True)
    play_count = models.IntegerField(null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.song}'
