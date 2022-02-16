from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Playlist(models.Model):
    playlist_author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    cover = models.ImageField(null=True, upload_to="")
    create_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Maker(models.Model):
    name = models.CharField(max_length=30)
    cover = models.FileField(null=True)
    create_date = models.DateTimeField(null=True)


