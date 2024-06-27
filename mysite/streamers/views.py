from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Streamer

def index(request):
    total_streamers = len(Streamer.objects.all())
    streamers_data= Streamer.objects.all()
    context = {"streamers_data": streamers_data, "total_streamers": total_streamers}
    return render(request, "streamers/index.html", context)

def streamers_list(request):
    streamers_data= Streamer.objects.all()
    context = {"streamers_data": streamers_data}
    return render(request, "streamers/streamers_list.html", context)

def detail(request, streamer_id):
    streamer = get_object_or_404(Streamer, pk=streamer_id)
    return render(request, "streamers/detail.html", {"streamer": streamer})

def about(request):
    return render(request, "streamers/about.html")