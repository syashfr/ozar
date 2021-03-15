from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Design(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    file = models.FileField(upload_to='designFiles/')
    tags = TaggableManager()
