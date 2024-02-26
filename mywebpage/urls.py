from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about",views.about, name="about"),
    path("download/<int:file_id>/", views.FileDownloadView.as_view(), name="file_download"),
    path("projects", views.ProjectsView.as_view(), name = "projects"),
    path("contact/<int:pk>", views.ContactView.as_view(), name= "contact"),
    path("feedback", views.FeedBackView.as_view(), name="feedback"),
    path("all-comments", views.AllFeedbackView.as_view(), name = "allcomments"),
    path("thankyou", views.thankyou, name = "thankyou")
]

