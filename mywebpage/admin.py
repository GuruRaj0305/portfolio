from django.contrib import admin
from .models import MyDetail, Projects, FeedBack

# Register your models here.
class MyFileAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    pass

class FeedBackAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyDetail, MyFileAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
