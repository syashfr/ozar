from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    reviews = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='services/', blank=True)

    def __str__(self):
        return self.name