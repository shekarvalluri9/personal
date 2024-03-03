from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profession/", views.profession, name="profession"),
    path("profession.html", views.profession, name="profession_html")
]
