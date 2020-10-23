from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    price = models.FloatField(default=0.0, blank=True)
    reviews = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='services/', blank=True)
