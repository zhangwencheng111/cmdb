from django.shortcuts import render
from assets.models import Project
from assets.host_form import ProjectForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def projects_list(request):
	"""项目展示"""
	projects = Project.objects.all()
	content = {"projects_list":projects}
	return render(request, "assets/projects_list.html", content)


def one_project(request, project_id):
	"""单个项目信息"""
	project_one = Project.objects.get(id=project_id)
	content = {"project_one":project_one}
	return render(request, "assets/project.html", content)


def add_project(request):
	"""添加项目"""
	if request.method != "POST":
		form = ProjectForm()
	else:
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse("projects_list"))

	content = {"form":form}	
	return render(request, "assets/add_project.html", content)


def edit_project(request, project_id):
	"""编辑"""
	project = Project.objects.get(id=project_id)

	if request.method != "POST":
		form = ProjectForm(instance=project)
	else:
		form = ProjectForm(instance=project, data=request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse("projects_list"))

	content = {"form":form, "project":project}
	return render(request, "assets/edit_project.html", content)