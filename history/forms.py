from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):

  class Meta:
      model = Artist
      fields = ('name', 'birth_date', 'biggest_hit')


class SongForm(forms.ModelForm):

  class Meta:
      model = Song
      fields = ('title', 'album', 'artist')
