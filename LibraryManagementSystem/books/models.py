from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)
    pages = models.IntegerField()
    published_date = models.DateField()

    def __str__(self):
        return self.title