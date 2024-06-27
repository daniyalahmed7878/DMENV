from django.db import models
class Carousel(models.Model):
    caption= models.CharField(max_length=30)
    description = models.TextField()
    image = models.FileField(max_length=300, upload_to="carousel/", null=True)
# Create your models here.
