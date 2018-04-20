from django.db import models
from assets.models import Host, Project
from django import forms

class HostForm(forms.ModelForm):
	class Meta:
		model = Host
		fields = '__all__'
		widgets = {
		"editor": forms.Textarea(attrs={'cols': 50, 'rows': 10}),
		}


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = '__all__'