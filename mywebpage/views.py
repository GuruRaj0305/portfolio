from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import MyDetail, Projects, FeedBack
from django.views.generic import ListView, DetailView
from .forms import FeedBackForm
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, "mywebpage/home.html")


def about(request):
    return render(request, "mywebpage/about.html")

class FileDownloadView(View):
    def get(self, request, file_id):
        my_file = get_object_or_404(MyDetail, pk=file_id)
        file_path = my_file.resume.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(my_file.resume.name)
        return response
    

class ProjectsView(ListView):
    template_name = "mywebpage/projects.html"
    model = Projects
    context_object_name = "projects"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-pk")
        return data
    
class ContactView(DetailView):
    template_name = "mywebpage/contact.html"
    model = MyDetail
    

class FeedBackView(View):
    def get(self, request):
        form = FeedBackForm()
        return render(request, "mywebpage/feedback.html", {
            "form": form
        })
    
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thankyou")
        return HttpResponseRedirect("feedback")
    
class AllFeedbackView(ListView):
    template_name = "mywebpage/every_feedback.html"
    model = FeedBack
    context_object_name = "feedbacks"

def thankyou(request):
    return render(request, "mywebpage/submited.html")