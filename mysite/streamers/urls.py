from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("streamer/", views.streamers_list, name="streamers_list"),
    path("streamer/<int:streamer_id>/", views.detail, name="detail"),
    path("about/", views.about, name="about"),
]