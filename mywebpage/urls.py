from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about",views.about, name="about"),
    path('download/<int:file_id>/', views.FileDownloadView.as_view(), name='file_download'),
]
