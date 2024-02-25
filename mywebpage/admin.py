from django.contrib import admin
from .models import MyFile, Projects

# Register your models here.
class MyFileAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyFile, MyFileAdmin)
admin.site.register(Projects, ProjectsAdmin)
