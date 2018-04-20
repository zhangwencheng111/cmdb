from django.db import models


class Dev_Script(models.Model):
	"""脚本执行表单"""
	GRP_CHIOSE = [(i, i) for i in ["生产", "预发", "测试", "开发中"]]
	PARA_NUM_CHOICES = [(i, i) for i in range(11)]
	TYPE_CHOICES = (
		("python", "python"),
		("sell", "sell"),
		("fabric", "fabric"),
		("ansible", "ansible")
		)

	function_detail = models.CharField(max_length=30, verbose_name="脚本功能", unique=True)
	script_type = models.CharField(max_length=10, verbose_name="脚本类型", choices=TYPE_CHOICES)
	env = models.CharField(max_length=20, verbose_name="脚本执行环境", choices=GRP_CHIOSE)
	script_dir = models.CharField(max_length=100, verbose_name="脚本路径", blank=True)
	#模板这里如何执行脚本 ；比如fab -f script_dir deploy
	cmd_template = models.CharField(max_length=100, verbose_name="命令模板", blank=True)
	parameter_num = models.IntegerField(verbose_name="参数个数", choices=PARA_NUM_CHOICES, default=0)
	editor = models.TextField(verbose_name="备注", blank=True)
	date_added = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")

	class Meta:
		verbose_name = "自动化脚本"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.function_detail