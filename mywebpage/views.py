from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import MyFile, Projects
from django.views.generic import ListView



# Create your views here.

def home(request):
    return render(request, "mywebpage/home.html")


def about(request):
    return render(request, "mywebpage/about.html")

class FileDownloadView(View):
    def get(self, request, file_id):
        my_file = get_object_or_404(MyFile, pk=file_id)
        file_path = my_file.file.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(my_file.file.name)
        return response
    

class ProjectsView(ListView):
    template_name = "mywebpage/projects.html"
    model = Projects
    context_object_name = "projects"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-pk")
        return data
    
