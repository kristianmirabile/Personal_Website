from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    text = models.TextField(max_length=10000)
    date = models.DateField()

def __str__(self):
    return self.title