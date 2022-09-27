from django.shortcuts import render, redirect
from projects.models import Project, Tag, Review
from projects.forms import ProjectForm
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


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    context = {'create_project_form':form}

    return render(request, 'projects/create_project.html',context)


def edit_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(".")
    context = {'edit_project_form':form}

    return render(request, 'projects/edit_project.html',context)


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()

    return redirect("list_projects")
