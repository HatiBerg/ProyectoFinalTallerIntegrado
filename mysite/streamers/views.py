from django.http import HttpResponse
from django.shortcuts import render

from .models import Streamer

def index(request):
    latest_question_list = Streamer.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "streamers/index.html", context)

def detail(request):
    latest_question_list = Streamer.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "streamers/detail.html", context)

def about(request):
    latest_question_list = Streamer.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "streamers/about.html", context)