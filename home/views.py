from django.shortcuts import render
from .models import Playlist
# Create your views here.



def index(request):
    """
    playlist 목록 출력
    """
    playlist_list = Playlist.objects.order_by('-create_date')
    context = {'playlist_list': playlist_list}
    return render(request, 'home/playlist_list.html', context)