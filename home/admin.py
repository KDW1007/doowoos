from django.contrib import admin
from .models import Playlist, Maker
# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Maker)
