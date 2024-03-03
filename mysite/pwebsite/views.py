from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pwebsite/layout.html')

def profession(request):
    title = "movie-name"
    context = {'title':title}
    
    return render(request, "pwebsite/profession.html", context)
