from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    # path('artists/', views.ArtistListTemplateView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artists/add/', views.ArtistFormView.as_view(), name='artist_form'),
]
