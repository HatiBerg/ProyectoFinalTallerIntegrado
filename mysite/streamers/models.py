from django.db import models

class Streamer(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    most_streamed_game = models.CharField(max_length=100)
    average_stream_duration	 = models.FloatField()
    followers_gained_per_stream = models.FloatField()
    avg_viewers_per_stream = models.FloatField()
    avg_games_per_stream = models.FloatField()
    total_time_streamed = models.FloatField()
    total_followers = models.IntegerField()
    total_views = models.IntegerField()
    total_games_streamed = models.IntegerField()
    active_days_per_week = models.FloatField()
    most_active_day = models.CharField(max_length=10)
    day_with_most_followers_gained = models.CharField(max_length=10)