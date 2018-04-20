from django.db import models

class Install_List(models.Model):
	"""装机列表"""

	TYPR_CHOICE = (
		(0, "惠普"),
		(1, "戴尔"),
		)

	OS_CHOICE = (
		(0, "Centos6"),
		(1, "Centos7"),
	)

	STATUS = (
		(0, "未安装"),
		(1, "已安装"),
		)

	server_type = models.IntegerField(verbose_name="服务器类型", choices=TYPR_CHOICE)
	os = models.IntegerField(verbose_name="操作系统", choices=OS_CHOICE, default=1)

	sn_number = models.CharField(max_length=50, verbose_name="SN号", unique=True)
	server_cabinet = models.CharField(max_length=20, verbose_name="服务器机柜")
	location = models.IntegerField(verbose_name="起始位置")
	ilo_ip = models.GenericIPAddressField(verbose_name="管理IP", unique=True)

	hostname = models.CharField(max_length=50, verbose_name="主机名")
	dns = models.GenericIPAddressField(verbose_name="DNS")
	gateway = models.GenericIPAddressField(verbose_name="网关")
	mac_addr = models.CharField(max_length=50, verbose_name="网卡")
	addr_type = models.CharField(max_length=50, verbose_name="配置类型")
	status = models.IntegerField(verbose_name="安装状态", choices=STATUS, default=0)