from django.db import models
from dev.models import Dev_Script
from django import forms
from assets.models import Project

class Script_Form(forms.ModelForm):
	
	class Meta:
		model = Dev_Script
		fields = '__all__'
		widgets = {
		"editor": forms.Textarea(attrs={'cols': 50, 'rows': 10}),
		}

"""
class Project_Form(forms.Form):
	project = forms.ModelChoiceField(label="", queryset=None,)
	
	def __init__(self, *args, **kwargs):
		super(Project_Form, self).__init__(*args, **kwargs)
		self.fields['project'].queryset = Project.objects.all()
"""