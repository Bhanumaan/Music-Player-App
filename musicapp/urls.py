from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('', views.all_songs, name='all_songs'),
    path('second/', views.all_songs_second, name='all_songs_2'),
    path('<int:song_id>/', views.detail, name='detail'),
    path('detail_2/<int:song_id>/', views.detail_2, name='detail_2'),

    path('recent/', views.recent, name='recent'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('play_2/<int:song_id>/', views.play_song_2, name='play_song_2'),
    path('play_song/<int:song_id>/', views.play_song_index, name='play_song_index'),
    path('play_song/<int:song_id>/', views.play_song_index_2, name='play_song_index_2'),
    path('play_recent_song/<int:song_id>/', views.play_recent_song, name='play_recent_song'),
    path('play_recent_song_2/<int:song_id>/', views.play_recent_song_2, name='play_recent_song_2'),

    

]
