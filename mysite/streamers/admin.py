from django.contrib import admin

from .models import Streamer

class StreamerAdmin(admin.ModelAdmin):
    list_display = ["name", "language"]


admin.site.register(Streamer)