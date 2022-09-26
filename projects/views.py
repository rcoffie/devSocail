from django.shortcuts import render
from projects.models import Project, Tag, Review
# Create your views here.


def list_projects(request):
    list_projects = Project.objects.all()
    context = {'list_projects':list_projects}

    return render(request,'projects/list_projects.html',context )

def project_detail(request, id):

    project_detail = Project.objects.get(id=id)
    tags = project_detail.tags.all()
    context = {'project_detail':project_detail,'tags':tags,}

    return render(request, 'projects/project_detail.html',context)
