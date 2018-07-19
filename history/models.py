from django.db import models

class Artist(models.Model):
  name = models.TextField(default="")
  birth_date = models.TextField(default="")
  biggest_hit = models.TextField(default="")

class Song(models.Model):
  title = models.TextField(default="")
  album = models.TextField(default="")
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, )
