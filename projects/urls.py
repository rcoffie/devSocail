from django.urls import path, include
from projects.views import (list_projects, project_detail)

urlpatterns = [
    path("list-projects/",list_projects,name="list_projects"),
    path("project-detail/<str:id>/", project_detail,name="project_detail")
]
