from django.test import TestCase

from projects.models import Project, Review, Tag

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
