from django.test import TestCase
from django.urls import reverse
from projects.models import Project, Review, Tag


class TestCreateProjectView(TestCase):


    def test_project_list_view(self):
        response = self.client.get(reverse('list_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/list_projects.html')

    def test_project_detail_view(self):
        project = Project.objects.create(title="title",description="description",demo_link="demo_link")
        response = self.client.get(reverse('project_detail', kwargs={'id': Project.objects.first().id}))
        # kwargs={'unique_id': RandomModel.objects.first().unique_id}

    def test_delete_project_view(self):
        project = Project.objects.create(title="title",description="description",demo_link="demo_link")
        response = self.client.get(reverse('delete_project',kwargs={'id': Project.objects.first().id}))

    def test_create_project(self):
        data = {
        'title':'title',
        'description':'description',
        'demo_link':'demo_link',
        }
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_project.html')
        confirm_response = self.client.post(reverse("create_project"), data=data)
        self.assertRedirects(confirm_response, reverse('list_projects'))

    def test_edit_project(self):
        project = Project.objects.create(title="title",description="description")
        data = {
        "title":"title",
        "descripition":"descripition update",

        }
        url = self.client.get(reverse("edit_project", kwargs={'id': Project.objects.first().id}))
        self.assertTemplateUsed(url, 'projects/edit_project.html')
        response = self.client.post(reverse('edit_project',kwargs={'id': Project.objects.first().id}),data=data)
        self.assertEqual(response.status_code, 302)
