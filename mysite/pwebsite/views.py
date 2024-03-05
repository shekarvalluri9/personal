from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pwebsite/layout.html')

def profession(request):
    title = "Profession"
    return render(request, "pwebsite/profession.html", {"title":title})
def education(request):
    title ="Education"
    return render(request, "pwebsite/education.html",{"title":title})
def activities(request):
    title = "Activities"
    return render(request, "pwebsite/activities.html", {"title":title})

def home(request):
    return render(request, "pwebsite/layout.html")