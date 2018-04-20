import os
import sys
from fabric.api import *

env.user = "abc"
env.hosts = []
env.password = "xxx"
env.port = 22

start = "/etc"
name = "passwd"

def findfile():
	"""查找文件"""
	start = "/etc"
	name = "passwd"
	for path, dir, filename in os.walk(start):
		if name in filename:
			full_name = os.path.join(path, name)
			print(os.path.normpath(os.path.abspath(full_name)))
			return os.path.normpath(os.path.abspath(full_name))

@parallel(pool_size=4)
def deploy(start, name, parameter=""):
	"""远程上传脚本并执行"""
	remote_tmp_dir = "/tmp"
	name_dir = findfile(start, name)
	if not name_dir:
		raise SystemExit("there isn't targe file")
	else:
		put(name_dir, remote_tmp_dir)
		with cd("/tmp"):
			sudo("/bin/bash {name} {parameter}".format(name=name, parameter=parameter))