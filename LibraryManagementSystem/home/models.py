from django.db import models

# Create your models here.

from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
