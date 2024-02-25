from django.contrib import admin
from .models import MyFile

# Register your models here.
class MyFileAdmin(admin.ModelAdmin):
    list_display = ("file",)

admin.site.register(MyFile, MyFileAdmin)