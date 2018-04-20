from django.shortcuts import render
from dev.models import Dev_Script
from dev.forms import Script_Form
from assets.models import Project
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import subprocess
from assets.models import Host
from django.http import JsonResponse


def show_script(request):
	"""展示脚本"""
	if request.method == "GET":
		project = Project.objects.all()
		script_name = Dev_Script.objects.order_by("-date_added")
		context = {"script_name":script_name, "project":project}
		return render(request, "dev/show_script.html", context)
	elif request.method == "POST":
		project_name = request.POST.get("name")
		context = {"status": 200, "message": "ok", "1":project_name}
		return JsonResponse(context)


def add_script(request):
	"""添加"""
	if request.method != "POST":
		form = Script_Form()
	else:
		form = Script_Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("dev:show_script"))

	context = {"form":form}
	return render(request, "dev/add_script.html", context)


def execute_srcipt(request, script_id):
	"""执行脚本"""
	script = Dev_Script.objects.get(id=script_id)
	#执行脚本，并且输出信息
	try:
		#暂时没加参数
		exec_meg = subprocess.check_output(script.cmd_template, stderr=subprocess.STDOUT, shell=True)
		#exec_meg = subprocess.check_output("ls -al", stderr=subprocess.STDOUT, shell=True)  测试用的.
	except subprocess.CalledProcessError as e:
		exec_meg = e.output
		code = e.returncode

	context = {"message":exec_meg, "script":script}
	return render(request, "dev/execute_srcipt.html", context)


def edit_script(request, script_id):
	"""编辑"""
	script = Dev_Script.objects.get(id=script_id)
	if request.method != "POST":
		form = Script_Form(instance=script)
	else:
		form = Script_Form(instance=script, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("dev:show_script"))

	context = {"form":form, "script":script}
	return render(request, "dev/edit_script.html", context)


def ip_choise(request):
	"""选择ip界面"""
	if request.method == "POST":
		project_id = request.POST.get("dd")
		project = Project.objects.get(id=project_id)
		hosts = project.host_set.all()
		context = {"project":project,"hosts":hosts}
		return render(request, "dev/ip_choise.html", context)