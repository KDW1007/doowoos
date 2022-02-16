from django.db import models
# Create your models here.

class Author(models.Model):
    name = models.CharField(null=False, max_length=30)
    cover = models.FileField(null=True)

class Books(models.Model):
    cover = models.FileField(null=True)
    book_title = models.CharField(null=False, max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    intro = models.TextField(null=True)
    upload_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Chapter(Books):
    chapter_title = models.CharField(null=False, max_length=100)
    chapter_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField(null=True)
    contents = models.TextField(null=True)
    reading_time = models.IntegerField(null=True)

