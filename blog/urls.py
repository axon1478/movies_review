from django.conf.urls import url
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [

    path('about/', AboutView.as_view(), name='blog-about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/<str:name>/<int:id>/', PostCreateView.as_view(), name='post-create'),
    path('', MoviesListView.as_view(), name='blog-home'),
    path('<str:name>/<int:pk>/', MoviesDetailListView.as_view(), name='movies-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('action/', ActionView.as_view(), name='gean-action'),
    path('sifi/', SifiView.as_view(), name='gean-sifi'),
    path('thriller/', ThrillerView.as_view(), name='gean-thriller'),
    path('adventure/', AdventureView.as_view(), name='gean-adventure'),
    path('classic/', ClassicView.as_view(), name='gean-classic'),
    path('Romance/', RomanceView.as_view(), name='gean-romance'),
    path('animation/', AnimationView.as_view(), name='gean-animation'),
    path('drama/', DramaView.as_view(), name='gean-drama'),
    path('crime/', CrimeView.as_view(), name='gean-crime'),
    path('mystery/', MysteryView.as_view(), name='gean-mystery'),
    path('family/', FamilyView.as_view(), name='gean-family'),
    path('documentary/', DocumentaryView.as_view(), name='gean-documentary'),
    path('fantasy/', FantasyView.as_view(), name='gean-fantacy'),
    path('comedy/', ComedyView.as_view(), name='gean-comedy'),

    path('search/', SearchView, name='search'),

    path('movies/', GeansMoviesView.as_view(), name='movies'),
    path('movies/action/', ActionMoviesView.as_view(), name='gean-movies-action'),
    path('movies/sifi/', SifiMoviesView.as_view(), name='gean-movies-sifi'),
    path('movies/thriller/', ThrillerMoviesView.as_view(), name='gean-movies-thriller'),
    path('movies/adventure/', AdventureMoviesView.as_view(), name='gean-movies-adventure'),
    path('movies/classic/', ClassicMoviesView.as_view(), name='gean-movies-classic'),
    path('movies/Romance/', RomanceMoviesView.as_view(), name='gean-movies-romance'),
    path('movies/animation/', AnimationMoviesView.as_view(), name='gean-movies-animation'),
    path('movies/drama/', DramaMoviesView.as_view(), name='gean-movies-drama'),
    path('movies/crime/', CrimeMoviesView.as_view(), name='gean-movies-crime'),
    path('movies/mystery/', MysteryMoviesView.as_view(), name='gean-movies-mystery'),
    path('movies/family/', FamilyMoviesView.as_view(), name='gean-movies-family'),
    path('movies/documentary/', DocumentaryMoviesView.as_view(), name='gean-movies-documentary'),
    path('movies/fantasy/', FantasyMoviesView.as_view(), name='gean-movies-fantacy'),
    path('movies/comedy/', ComedyMoviesView.as_view(), name='gean-movies-comedy'),

    path('series/', GeansSeriesView.as_view(), name='series'),
    path('series/action/', ActionSeriesView.as_view(), name='gean-series-action'),
    path('series/sifi/', SifiSeriesView.as_view(), name='gean-series-sifi'),
    path('series/thriller/', ThrillerSeriesView.as_view(), name='gean-series-thriller'),
    path('series/adventure/', AdventureSeriesView.as_view(), name='gean-series-adventure'),
    path('series/classic/', ClassicSeriesView.as_view(), name='gean-series-classic'),
    path('series/Romance/', RomanceSeriesView.as_view(), name='gean-series-romance'),
    path('series/animation/', AnimationSeriesView.as_view(), name='gean-series-animation'),
    path('series/drama/', DramaSeriesView.as_view(), name='gean-series-drama'),
    path('series/crime/', CrimeSeriesView.as_view(), name='gean-series-crime'),
    path('series/mystery/', MysterySeriesView.as_view(), name='gean-series-mystery'),
    path('series/family/', FamilySeriesView.as_view(), name='gean-series-family'),
    path('series/documentary/', DocumentarySeriesView.as_view(), name='gean-series-documentary'),
    path('series/fantasy/', FantasySeriesView.as_view(), name='gean-series-fantacy'),
    path('series/comedy/', ComedySeriesView.as_view(), name='gean-series-comedy'),

]
