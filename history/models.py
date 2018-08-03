from django.db import models

class Artist(models.Model):
  name = models.CharField(default="", max_length=100)
  birth_date = models.CharField(default="", max_length=100)
  biggest_hit = models.CharField(default="", max_length=100)

  def __str__(self):
    return self.name

class Song(models.Model):
  title = models.CharField(default="", max_length=100)
  album = models.CharField(default="", max_length=100)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, )
