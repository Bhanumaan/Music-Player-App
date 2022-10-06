from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
    # Display recent songs
    if not request.user.is_anonymous:
        recent = list(Recent.objects.all().values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent][:5]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    # Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.all().values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            first_time = True
            last_played_song = Song.objects.get(id=7)

    else:
        first_time = True
        last_played_song = Song.objects.get(id=7)

    # Display all songs
    songs = Song.objects.all()

    # Display few songs on home page
    songs_all = list(Song.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song.objects.filter(id__in=sliced_ids)

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(name__icontains=search_query)).distinct()
        context = {'all_songs': filtered_songs, 'last_played': last_played_song, 'query_search': True}
        return render(request, 'musicapp/index.html', context)

    context = {
        'all_songs': indexpage_songs,
        'recent_songs': recent_songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'query_search': False,
    }
    return render(request, 'musicapp/index.html', context=context)


def index_2(request):
    # Display recent songs
    if not request.user.is_anonymous:
        recent = list(Recent.objects.all().values('song_id').order_by('-id'))
        recent_id = [each['song_id'] for each in recent][:5]
        recent_songs_unsorted = Song2.objects.filter(id__in=recent_id)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    # Last played song
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.all().values('song_id').order_by('-id'))
        if last_played_list:
            last_played_id = last_played_list[0]['song_id']
            last_played_song = Song2.objects.get(id=last_played_id)
        else:
            first_time = True
            last_played_song = Song2.objects.get(id=2)

    else:
        first_time = True
        last_played_song = Song2.objects.get(id=2)

    # Display all songs
    songs = Song2.objects.all()

    # Display few songs on home page
    songs_all = list(Song2.objects.all().values('id').order_by('?'))
    sliced_ids = [each['id'] for each in songs_all][:5]
    indexpage_songs = Song2.objects.filter(id__in=sliced_ids)

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = songs.filter(Q(name__icontains=search_query)).distinct()
        context = {'all_songs': filtered_songs, 'last_played': last_played_song, 'query_search': True}
        return render(request, 'musicapp/all_songs_2.html', context)

    context = {
        'all_songs': indexpage_songs,
        'recent_songs': recent_songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'query_search': False,
    }
    return render(request, 'musicapp/all_songs_2.html', context=context)


def play_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    print("data")
    print(data)
    data.save()
    return redirect('all_songs')


def play_song_2(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    print("data")
    print(data)
    data.save()
    return redirect('all_songs_2')


def play_song_index(request, song_id):
    songs = Song.objects.filter(id=song_id)
    # Add data to recent database
    print(songs.id)
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    data.save()
    return redirect('index')


def play_song_index_2(request, song_id):
    songs = Song.objects.filter(id=song_id)
    # Add data to recent database
    print(songs.id)
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    data.save()
    return redirect('index')


def play_recent_song(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    data.save()
    return redirect('recent')


def play_recent_song_2(request, song_id):
    songs = Song2.objects.filter(id=song_id).first()
    # Add data to recent database
    if list(Recent.objects.filter(song=songs).values()):
        data = Recent.objects.filter(song=songs)
        data.delete()
    data = Recent(song=songs)
    data.save()
    return redirect('recent')


def all_songs(request):
    songs = Song.objects.all()
    first_time = False
    last_played_list = list(Recent.objects.all().values('song_id').order_by('-id'))
    if first_time == True:
        last_played_song = Song.objects.get(id=7)
        last_played_id = last_played_song[0]['song_id']
    else:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    # apply search filters
    qs_singers = Song.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    all_singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        search_singer = request.GET.get('singers') or ''
        filtered_songs = songs.filter(Q(name__icontains=search_query)).filter(
            Q(singer__icontains=search_singer)).distinct()
        context = {
            'songs': filtered_songs,
            'last_played': last_played_song,
            'all_singers': all_singers,
            'query_search': True,
        }
        return render(request, 'musicapp/all_songs.html', context)
    context = {
        'songs': songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'all_singers': all_singers,
        'query_search': False,
    }
    return render(request, 'musicapp/all_songs.html', context=context)


def all_songs_second(request):
    songs = Song2.objects.all()
    first_time = False
    last_played_list = list(Recent.objects.all().values('song_id').order_by('-id'))
    print(last_played_list)
    if first_time == True:
        last_played_song = Song2.objects.all().filter(id=3)
        last_played_id = last_played_song[0]['song_id']
    else:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song2.objects.get(id=last_played_id)
    # apply search filters
    qs_singers = Song2.objects.values_list('singer').all()
    s_list = [s.split(',') for singer in qs_singers for s in singer]
    all_singers = sorted(list(set([s.strip() for singer in s_list for s in singer])))
    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        search_singer = request.GET.get('singers') or ''
        filtered_songs = songs.filter(Q(name__icontains=search_query)).filter(
            Q(singer__icontains=search_singer)).distinct()
        context = {
            'songs': filtered_songs,
            'last_played': last_played_song,
            'all_singers': all_singers,
            'query_search': True,
        }
        return render(request, 'musicapp/all_songs_2.html', context)
    context = {
        'songs': songs,
        'last_played': last_played_song,
        'first_time': first_time,
        'all_singers': all_singers,
        'query_search': False,
    }
    return render(request, 'musicapp/all_songs_2.html', context=context)


def recent(request):
    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    # Display recent songs
    recent = list(Recent.objects.all().values('song_id').order_by('-id'))
    if recent:
        recent_id = [each['song_id'] for each in recent]
        recent_songs_unsorted = Song.objects.filter(id__in=recent_id)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    elif recent:
        recent_id = [each['song_id'] for each in recent]
        recent_songs_unsorted = Song2.objects.filter(id__in=recent_id)
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent_songs = None

    if len(request.GET) > 0:
        search_query = request.GET.get('q')
        filtered_songs = recent_songs_unsorted.filter(Q(name__icontains=search_query)).distinct()
        context = {'recent_songs': filtered_songs, 'last_played': last_played_song, 'query_search': True}
        return render(request, 'musicapp/recent.html', context)

    context = {'recent_songs': recent_songs, 'last_played': last_played_song, 'query_search': False}
    return render(request, 'musicapp/recent.html', context=context)


def detail(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    data = Recent(song=songs)
    data.save()

    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    playlists = Playlist.objects.all().values('playlist_name').distinct
    is_favourite = Favourite.objects.all().filter(song=song_id).values('is_fav')

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")
        elif 'add-fav' in request.POST:
            is_fav = True
            query = Favourite(user=request.user, song=songs, is_fav=is_fav)
            print(f'query: {query}')
            query.save()
            messages.success(request, "Added to favorite!")
            return redirect('detail', song_id=song_id)
        elif 'rm-fav' in request.POST:
            is_fav = True
            query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
            print(f'user: {request.user}')
            print(f'song: {songs.id} - {songs}')
            print(f'query: {query}')
            query.delete()
            messages.success(request, "Removed from favorite!")
            return redirect('detail', song_id=song_id)

    context = {'songs': songs, 'playlists': playlists, 'is_favourite': is_favourite, 'last_played': last_played_song}
    return render(request, 'musicapp/detail.html', context=context)


def detail_2(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    print(type(songs))
    print(songs)
    print(songs.id)

    data = Recent(song=songs)
    data.save()
    # Last played song
    last_played_list = list(Recent.objects.values('song_id').order_by('-id'))
    if last_played_list:
        last_played_id = last_played_list[0]['song_id']
        last_played_song = Song.objects.get(id=last_played_id)
    else:
        last_played_song = Song.objects.get(id=7)

    if request.method == "POST":
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q = Playlist(user=request.user, song=songs, playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")
        elif 'add-fav' in request.POST:
            is_fav = True
            query = Favourite(user=request.user, song=songs, is_fav=is_fav)
            print(f'query: {query}')
            query.save()
            messages.success(request, "Added to favorite!")
            return redirect('detail', song_id=song_id)
        elif 'rm-fav' in request.POST:
            is_fav = True
            query = Favourite.objects.filter(user=request.user, song=songs, is_fav=is_fav)
            print(f'user: {request.user}')
            print(f'song: {songs.id} - {songs}')
            print(f'query: {query}')
            query.delete()
            messages.success(request, "Removed from favorite!")
            return redirect('detail', song_id=song_id)

    context = {'songs': songs, 'last_played': last_played_song}
    return render(request, 'musicapp/detail_2.html', context=context)




