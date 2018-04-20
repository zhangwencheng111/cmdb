from django.shortcuts import render
from install.models import Install_List


def install_list(request):
	"""展示列表"""
	lists = Install_List.objects.filter(status=0).all()
	context = {"lsits": lists}
	return render(request, "install/install_list.html", context)