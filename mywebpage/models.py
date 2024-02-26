from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class MyDetail(models.Model):
    resume = models.FileField(upload_to='resume')
    name = models.CharField(max_length = 50, null = True)
    insta_id = models.CharField(max_length = 400, null = True)
    whatspp_num = models.CharField(max_length = 12,null = True)
    linkedin_id = models.CharField(max_length = 400, null = True)
    github_id = models.CharField(max_length = 400, null = True)
    email_id = models.EmailField(null = True)




class Projects(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to= "images")
    discription = models.TextField(validators = [MinLengthValidator(10)])
    link = models.CharField(max_length = 400, default="https://github.com/GuruRaj0305")

class FeedBack(models.Model):
    user_name = models.CharField(max_length = 100)
    user_mail_id = models.EmailField()
    user_mobile_number = models.CharField(max_length = 12,null = True)
    user_feedback = models.TextField()