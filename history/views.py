from django.shortcuts import render, get_object_or_404
from history.models import Artist, Song

def artists(request):
  artist_list = Artist.objects.all()
  print("artist list??", artist_list)
  context = {"artists": artist_list}
  return render(request, 'history/artists.html', context) # Is request needed in order to complete the req/res cycle?

def new_artist(request):
  print(request.POST)
  # Create a new record using the model's constructor.
  # Artist.create(request.POST)

def detail(request, artist_id):
  print("this is a detail request")
  artist = get_object_or_404(Artist, pk=artist_id)
  # Can get related songs a couple of ways:
  # songs = Song.objects.filter(artist_id=artist_id)
  # or...
  songs = artist.song_set.all()
  return render(request, 'history/detail.html', {"artist": artist, "songs": songs})
