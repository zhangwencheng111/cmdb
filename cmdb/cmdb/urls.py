"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from assets import views, project_view
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views as users_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^hosts/$', views.hosts, name="hosts"),
    url(r'^host/(?P<host_uuid>.*)/$', views.host, name="host"),
    url(r'^add_host/$', views.add_host, name="add_host"),
    url(r'^edit_host/(?P<host_uuid>.*)/$', views.edit_host, name="edit_host"),
    url(r'^users/login/$', auth_views.login, {'template_name': 'users/login.html'},name="login"),
    url(r'^users/logout/$', users_view.user_logout, name="logout"),
    url(r'^projects/$', project_view.projects_list, name="projects_list"),
    url(r'^project/(?P<project_id>.*)/$', project_view.one_project, name="one_project"),
    url(r'^add_project/$', project_view.add_project, name="add_project"),
    url(r'^edit_project/(?P<project_id>.*)/$', project_view.edit_project, name="edit_project"),
    url(r'^dev/', include('dev.urls', namespace='dev')),
    url(r'^install/', include("install.urls", namespace='install')),
]