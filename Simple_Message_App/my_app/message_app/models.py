from django.db import models


class Post(models.Model):
    username= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    dateSubmitted = models.TextField()

