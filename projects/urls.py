from django.urls import include, path

from projects.views import (create_project, delete_project, edit_project,
                            list_projects, project_detail)

urlpatterns = [
    path("list-projects/",list_projects,name="list_projects"),
    path("project-detail/<str:id>/", project_detail,name="project_detail"),
    path('create-project/', create_project,name="create_project"),
    path('edit-project/<str:id>/', edit_project, name="edit_project"),
    path('delete-project/<str:id>/', delete_project, name="delete_project")
]
