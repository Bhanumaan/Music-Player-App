from django.db import models



# Create your models here.
class Song(models.Model):

    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name
class Song2(models.Model):

    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Recent_2(models.Model):
    song2 = models.ForeignKey(Song, on_delete=models.CASCADE)