from django.urls import path
from . import views

app_name = 'history'
# TODO: Replace with Router
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    # path('artists/', views.ArtistListTemplateView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/add/', views.ArtistFormView.as_view(), name='artist_form'),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('songs/add', views.SongFormView.as_view(), name='song_form'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('songs/<int:pk>/edit', views.SongEditView.as_view(), name='song_edit'),
    path('artists/add/', views.ArtistFormView.as_view(), name='artist_form'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/add/', views.AlbumFormView.as_view(), name='album_form'),
    path('albums/<int:pk>/edit', views.AlbumEditView.as_view(), name='album_edit'),
]
