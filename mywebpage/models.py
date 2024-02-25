from django.db import models

# Create your models here.
class MyFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.TextField()