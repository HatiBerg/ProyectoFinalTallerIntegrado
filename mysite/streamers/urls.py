from django.urls import path

from . import views

app_name = "streamers"
urlpatterns = [
    path("", views.index, name="index"),
    path("streamer/<int:streamer_id>/", views.detail, name="detail"),
    path("about/", views.about, name="about"),
]