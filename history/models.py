from django.db import models
from django.urls import reverse

class Artist(models.Model):
  name = models.CharField(default="", max_length=100)
  birth_date = models.CharField(default="", max_length=100)
  biggest_hit = models.CharField(default="", max_length=100)

  def __str__(self):
    return self.name

# Note that wrapping the model reference to Album_Songs in strings makes them evaluate lazily (after the models have been defined), to avoid 'not defined' errors
class Album(models.Model):
  title = models.CharField(max_length=100)
  year_released = models.CharField(max_length=4)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('history:album_detail', kwargs={'pk': self.pk})

class Song(models.Model):
  title = models.CharField(default="", max_length=100)
  albums = models.ManyToManyField(Album, blank=True)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, )

  def get_absolute_url(self):
    return reverse('history:song_detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.title


# class Album_Songs(models.Model):
#   album = models.ForeignKey(Album, on_delete=models.CASCADE, )
#   song = models.ForeignKey(Song, on_delete=models.CASCADE, )
