from django.conf.urls import url
from install import views


urlpatterns = [
	url(r'^$', views.install_list, name="install_list"),
]