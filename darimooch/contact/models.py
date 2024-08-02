from django.db import models
class Contact(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    message = models.TextField()
    
# Create your models here.
