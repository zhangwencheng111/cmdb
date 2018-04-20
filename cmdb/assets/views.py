from django.shortcuts import render
from assets.models import Host
from assets.host_form import HostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	"""主页"""
	return render(request, "assets/index.html")


def hosts(request):
	"""展示主机"""
	hosts_list = Host.objects.order_by("date_added")
	context = {"hosts_list":hosts_list}
	return render(request, "assets/hosts.html", context)


def host(request, host_uuid):
	"""主机信息"""
	alone_host = Host.objects.get(uuid=host_uuid)
	context = {"host":alone_host}
	return render(request, "assets/host.html", context)


def add_host(request):
	"""添加主机"""
	if request.method != "POST":
		form = HostForm()
	else:
		form = HostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("hosts"))

	context = {"form":form}
	return render(request, "assets/add_host.html", context)


def edit_host(request, host_uuid):
	"""编辑主机"""
	alone_host = Host.objects.get(uuid=host_uuid)

	if request.method != "POST":
		form = HostForm(instance=alone_host)
	else:
		form = HostForm(instance=alone_host, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("hosts"))

	context = {"form":form, "hosta":alone_host}
	return render(request, "assets/edit_host.html", context)