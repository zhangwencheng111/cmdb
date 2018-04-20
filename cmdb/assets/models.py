from django.db import models
import uuid


HOST_TYPE_CHOICES = (
	(u"物理机", u"物理机"),
	(u"虚拟机", u"虚拟机"),
	(u"云主机", u"云主机"),
	)


SYSTEM_TYPE_CHOICES = [(i, i) for i in (u"Centos", u"Windows")]


ENV_CHOICES = [(i, i) for i in (u"开发", u"测试", u"预发", u"生产")]


ETH_CHOICES = [(i, i) for i in range(1, 7)]


IDLE_CHOICES = [(i, i) for i in (u"使用中", u"空闲")]

PART_CHOICES = [(i, i) for i in ("开发", "运维", "架构")]


class Project(models.Model):
	"""项目"""
	project = models.CharField(max_length=50, verbose_name=u"项目名", unique=True)
	chinese_detail = models.CharField(max_length=20, verbose_name="中文描述")
	env = models.CharField(max_length=30, verbose_name="环境", choices=ENV_CHOICES)
	master = models.CharField(max_length=30, verbose_name="项目负责人", blank=True)
	department = models.CharField(max_length=10, verbose_name="部门", choices=PART_CHOICES, blank=True)

	class Meta:
		verbose_name = u"项目信息"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.project


class Host(models.Model):
	"""
	主机IP	
	主机名	
	主机类型：虚拟机还是物理机还是云主机	
	CPU	
	内存	
	硬盘
	系统类型
	环境	: 开发测试生产预发
	虚拟机父主机	
	所属项目
	网口	：123		
	状态	：使用中 空闲
	价格(RMB)	
	备注
	"""
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	ip_addr = models.GenericIPAddressField(verbose_name=u'IP地址', unique=True)
	host_name = models.CharField(max_length=100, blank=True, verbose_name=u'主机名')
	host_type = models.CharField(max_length=10, verbose_name=u'主机类型', choices=HOST_TYPE_CHOICES, default=u"虚拟机")
	cpu = models.CharField(max_length=10, blank=True, verbose_name=u"CPU")
	memery = models.CharField(max_length=10, blank=True, verbose_name=u"内存")
	hard_disk = models.CharField(max_length=40, blank=True, verbose_name=u"硬盘")
	system_type = models.CharField(max_length=20, verbose_name=u"操作系统", choices=SYSTEM_TYPE_CHOICES)
	environment = models.CharField(max_length=10, choices=ENV_CHOICES, verbose_name=u"环境")
	physical_host = models.ForeignKey("self", blank=True, null=True, verbose_name=u"虚拟机父主机")
	project = models.ManyToManyField(Project, blank=True, verbose_name=u"项目")
	eth_number = models.IntegerField(verbose_name=u"网口数", choices=ETH_CHOICES, default=1)
	idle = models.CharField(max_length=10, choices=IDLE_CHOICES, verbose_name=u"使用状态", blank=False, default=u"使用中")
	cost = models.IntegerField(blank=True, verbose_name=u"价格", default=0)
	editor = models.TextField(blank=True, verbose_name=u"备注")
	date_added = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")

	class Meta:
		verbose_name = u"主机"
		verbose_name_plural = verbose_name

	def __str__(self):
		if self.host_name:
			return "{}--{}".format(self.ip_addr, self.host_name)
		else:
			return self.ip_addr