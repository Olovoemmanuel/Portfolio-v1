from django.db import models

# Create your models here.

class Project(models.Model):
    Project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image')
    website_link = models.URLField()