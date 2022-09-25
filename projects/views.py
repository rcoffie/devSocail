from django.shortcuts import render
from projects.models import Project, Tag, Review
# Create your views here.


def list_projects(request):

    return render(request 'projects/list_projects.html')
