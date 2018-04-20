from django.conf.urls import url
from dev import views


urlpatterns = [
	url(r'^show_script/$', views.show_script, name="show_script"),
	url(r'^add_script/$', views.add_script, name="add_script"),
	url(r'^edit_script/(?P<script_id>\d+)/$', views.edit_script, name='edit_script'),
	url(r'^execute_srcipt/(?P<script_id>\d+)/$', views.execute_srcipt, name="execute_srcipt"),
	url(r'^ip_choise/$', views.ip_choise, name="ip_choise"),
]