from django.test import TestCase

from projects.models import Project, Review, Tag
from datetime import datetime

class TestProjectModel(TestCase):
    def setUp(self):
        project = Project.objects.create(title="title",description="description",demo_link="google.com",source_link="google.com")
        self.project = project
        review = Review.objects.create(project=self.project,body="body",value="value")
        self.review = review
        tag = Tag.objects.create(name="tag")
        self.tag = tag

    def test_project_str(self):
      self.assertEqual(self.project.title, 'title')
      self.assertEqual(str(self.project), 'title')

    def test_review_str(self):
        self.assertEqual(self.review.value, "value")
        self.assertEqual(str(self.review), "value")


    def test_tag_str(self):
        self.assertEqual(self.tag.name, "tag")
        self.assertEqual(str(self.tag), 'tag')


class ProjectModelFields(TestCase):
    def setUp(self):
        pass

    def test_project_model_fields(self):
        project = Project.objects.create(
        title = "title",
        description = "description",
        demo_link = "google.com",
        source_link = "google.com",
        featured_image = "img.jpg",
        vote_ratio = 1,
        vote_total = 1,
        created =datetime.now(),

        )

    def test_many_to_many_field(self):
        project = Project.objects.create(title="project title")
        tag1 = Tag.objects.create(name="laravel")
        tag2 = Tag.objects.create(name="django")
        project.tags.set([tag1.pk,tag2.pk])
        self.assertEqual(project.tags.count(), 2)


    def test_review_model_fields(self):
        project = Project.objects.create(title="title",description="description")
        review = Review.objects.create(
        project=project,body="body",value="value"
        )

    def test_tag_model_fields(self):
        tag = Tag.objects.create(name="name",created=datetime.now())
