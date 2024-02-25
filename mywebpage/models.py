from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class MyFile(models.Model):
    file = models.FileField(upload_to='resume')
    description = models.TextField()


class Projects(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to= "images")
    discription = models.TextField(validators = [MinLengthValidator(10)])
    link = models.CharField(max_length = 400, default="https://github.com/GuruRaj0305")