from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from history.models import Artist, Song
from history.forms import ArtistForm

class IndexView(TemplateView):
  template_name = 'history/index.html'

  def greeting(self):
    return {"msg": "Welcome to My Music Collection"}

# Below are two different ways of achieving the same result of a rendered view with generic class-based views
# 1) 'ArtistListTemplateView' subclasses TemplateView. Here we have to provide a template, and we can bind artist data to the template's 'view' property with the artist_list method we define on the class
# 2) 'ArtistListView' subclasses ListView. Here we don't point to a template. Django handles tfiguring that out by looking for one called 'artist_list' for us, and we bind the artist data to it by overriding the 'get_context_data' method that the ListView uses internally to find the data it needs to display for us in the DOM

#1)
class ArtistListTemplateView(TemplateView):
  template_name = 'history/artists.html'

  def artist_list(self):  # NOTE that it's the method name that becomes the property on 'view'
    artists = Artist.objects.all()
    return artists
#2)
class ArtistListView(ListView):
  model = Artist
  # Django defaults to referencing the data in the template as 'object_list'. Here is how we can rename it what we want
  context_object_name = 'artist_list'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

class ArtistFormView(FormView):
  template_name = 'history/artist_form.html'
  form_class = ArtistForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/artists/'

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super(ArtistFormView, self).form_valid(form)

# With a detail view you only need to provide the model. Django does everything else (as long as you've named your template `artist_detail`) But we want to also include all of the Artist's songs, to. So we have to add them to the context object that's bound to the template
class ArtistDetailView(DetailView):
  model = Artist

# ===============================
# Song Views

class SongListView(ListView):
  model = Song
  # Django defaults to referencing the data in the template as 'object_list'. Here is how we can rename it what we want
  context_object_name = 'song_list'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


# class SongFormView(FormView):
#   template_name = 'history/song_form.html'
#   form_class = SongForm
#   # NOTE! Be sure to put the slash in front of the url to route properly
#   success_url = '/history/songs/'

#   def form_valid(self, form):
#     # This method is called when valid form data has been POSTed.
#     # It should return an HttpResponse.
#     form.save()
#     return super(SongFormView, self).form_valid(form)


class SongDetailView(DetailView):
  model = Song
