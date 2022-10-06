from django import forms

from projects.models import Project, Review, Tag


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
