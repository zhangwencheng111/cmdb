from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def user_logout(request):
	"""登出"""
	logout(request)
	return HttpResponseRedirect(reverse("index"))