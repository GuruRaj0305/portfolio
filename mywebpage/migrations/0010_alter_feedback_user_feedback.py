# Generated by Django 5.0.2 on 2024-02-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebpage', '0009_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_feedback',
            field=models.TextField(),
        ),
    ]
