from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from .design_handler import plot_mesh
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Design(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='designFiles/')
    slug = models.SlugField(null=True)
    tags = TaggableManager()
    image = models.ImageField(blank=True)
    forked = models.BooleanField(default='False')
    forked_from = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("designspace:design", kwargs={
            'slug': self.slug
        })
    
    def get_3d_plot(self):
        file_path = self.file.path
        fig = plot_mesh(file_path)
        return fig

    def save(self, *args, **kwargs):
        value = self.author.get_username() + "-" + self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
    