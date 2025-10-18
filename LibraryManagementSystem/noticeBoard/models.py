from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    posted_date = models.DateField()

    def __str__(self):
        return self.title
