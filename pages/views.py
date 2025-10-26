from django.shortcuts import render
from projects.models import Project

# Create your views here.
def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {'featured_projects': featured_projects}
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')
