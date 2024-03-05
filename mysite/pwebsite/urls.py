from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profession/", views.profession, name="profession"),
    path("education/", views.education, name="education"),
    path("activities/", views.activities, name="activities"),
    path("home/", views.home, name="home")
]
