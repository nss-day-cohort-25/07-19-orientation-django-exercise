from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from history.models import Artist, Song, Album
from history.forms import ArtistForm, SongForm, AlbumForm

class IndexView(TemplateView):
  template_name = 'history/index.html'

  # "location" gets attached to a built-in object in the template called 'view'
  def location(self):
    return 'home'
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
    context["location"] = "artists"
    return context

class ArtistFormView(FormView):
  template_name = 'history/artist_form.html'
  form_class = ArtistForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/artists/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "add_artist"
    return context

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
    context["location"] = "songs"
    return context


class SongFormView(FormView):
  template_name = 'history/song_form.html'
  form_class = SongForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/songs/'

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super(SongFormView, self).form_valid(form)

class SongDetailView(DetailView):
  model = Song

class SongEditView(UpdateView):
  model = Song
  form_class = SongForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "song_edit"
    context["title_action"] = "Edit a song from"
    return context
  # template_name = 'history/song_form.html'

  # Not needed if relying on get_absolute_url from the Song model
  # def form_valid(self, form):
  #   # This method is called when valid form data has been POSTed.
  #   # It should return an HttpResponse.
  #   form.save()
  #   # To stay on the edit page:
  #   return self.render_to_response(self.get_context_data(form=form))

# ===============================
# Album Views

class AlbumListView(ListView):
  model = Album
  # Django defaults to referencing the data in the template as 'object_list'. Here is how we can rename it what we want
  context_object_name = 'album_list'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "albums"
    return context


class AlbumFormView(FormView):
  template_name = 'history/album_form.html'
  form_class = AlbumForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/albums/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "album_form"
    return context

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super(AlbumFormView, self).form_valid(form)

class AlbumDetailView(DetailView):
  model = Album

class AlbumEditView(UpdateView):
  model = Album
  form_class = AlbumForm
  template_name = 'history/album_form.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "album_edit"
    context["title_action"] = "Edit an album from"
    return context
