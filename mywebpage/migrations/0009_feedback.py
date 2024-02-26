# Generated by Django 5.0.1 on 2024-02-26 06:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebpage', '0008_rename_myfile_mydetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_mail_id', models.EmailField(max_length=254)),
                ('user_mobile_number', models.CharField(max_length=12, null=True)),
                ('user_feedback', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
    ]