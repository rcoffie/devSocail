from django.urls import path, include
from projects.views import (list_projects, project_detail, create_project, edit_project, delete_project)

urlpatterns = [
    path("list-projects/",list_projects,name="list_projects"),
    path("project-detail/<str:id>/", project_detail,name="project_detail"),
    path('create-project/', create_project,name="create_project"),
    path('edit-project/<str:id>/', edit_project, name="edit_project"),
    path('delete-project/<str:id>/', delete_project, name="delete_project")
]
