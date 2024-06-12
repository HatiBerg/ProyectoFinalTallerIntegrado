from django.db import models

class Streamers(models.Model):
    RANK = models.IntegerField()
    NAME = models.CharField(max_length=100)
    LANGUAGE = models.CharField(max_length=100)
    TYPE = models.CharField(max_length=100)
    MOST_STREAMED_GAME = models.CharField(max_length=100)
    AVERAGE_STREAM_DURATION	 = models.FloatField()
    FOLLOWERS_GAINED_PER_STREAM = models.FloatField()
    AVG_VIEWERS_PER_STREAM = models.FloatField()
    AVG_GAMES_PER_STREAM = models.FloatField()
    TOTAL_TIME_STREAMED = models.FloatField()
    TOTAL_FOLLOWERS = models.IntegerField()
    TOTAL_VIEWS = models.IntegerField()
    TOTAL_GAMES_STREAMED = models.IntegerField()
    ACTIVE_DAYS_PER_WEEK = models.FloatField()
    MOST_ACTIVE_DAY = models.CharField(max_length=10)
    DAY_WITH_MOST_FOLLOWERS_GAINED = models.CharField(max_length=10)