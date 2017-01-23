"""
供应商：
设备：
种类：
材料申请单：

关系：
供应商--提供多种--服务种类，服务种类--属于多个--供应商，之间的关系是多对多的关系
供应商--提供多个--设备，每台设备属于一个供应商，之间的关系是一对的关系 
每台设备由一个供应商提供，属于一个设备类型，

物资，单据，虚类
入库单，出库单由物资，单据，继承而来

"""


from django.db import models

# Create your models here.


class Supplier(models.Model):
	# 公司名称
	company_name = models.CharField("公司名称：",max_length=100)
	# 业务种类
	#categories = models.TextField()
	# 联系人
	contactor = models.CharField("联系人：",max_length=100)
	# 电话
	phone = models.CharField("手机：",max_length=100)
	# 邮箱
	email = models.EmailField("电子邮箱：")
	# 公司电话，或者传真
	company_phone = models.CharField("公司电话：",max_length=100)
	# 地址
	address = models.CharField("公司地址：",max_length=254)
	# 附件，例如：营业执照等
	attachments = models.FileField("三证附件：",upload_to='./uploads/%Y/%m/%d/')
	# 评价等级
	evaluation = models.CharField("评价等级：",max_length=100)
	# 摘要
	summary = models.TextField("公司经营范围：",)
	
	def __str__(self):
		return self.company_name
	
	class Meta(object):
		verbose_name='设备供应商'
		verbose_name_plural='设备供应商'
			

			
	
	
class Category(models.Model):
	# 种类名称
	category_name = models.CharField('种类名称', max_length=100)
	# 类别代码，设备，生活用品等分类
	category_code = models.IntegerField('类别代码')
	# 供应商可以提供多个种类服务，因此是多对多的关系
	suppliers = models.ManyToManyField(Supplier)
	# 摘要
	summary = models.TextField('摘要')
	
	def __str__(self):
		return ''.join([self.category_name, ':', self.category_code])
	class Meta:
		verbose_name='分类'
		verbose_name_plural = "分类"

	
	
class Device(models.Model):
	#设备来源
	bid = models.CharField('设备来源', max_length=100, default='自主采购')
	# 唯一性编号
	number = models.CharField('唯一性编号', max_length=100)
	# 设备类型，-----------外键
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='设备类型')
	# 设备名称
	name = models.CharField('设备名称', max_length=100)
	# 规格型号
	model = models.CharField('规格型号', max_length=100)
	# 出厂编号
	factory_id = models.CharField('出厂编号', max_length=100)
	# 参数
	parameters = models.TextField('参数')
	# 生产厂家
	manufactor = models.CharField('生产厂家', max_length=100)
	# 出厂日期
	release_date = models.DateField('出厂日期')
	# 购置日期
	acquisition_date = models.DateField('购置日期')
	# 启用日期
	received_date = models.DateField('启用日期')
	# 使用科室
	department = models.CharField('使用科室', max_length=100)
	# 保管人
	keeper = models.CharField('保管人', max_length=100)
	# 价值
	value = models.FloatField('价值')
	# 供应商,---------------外键 设备与供应商的关系是多对一的关系
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='供应商')
	# 备注
	demo = models.TextField('备注')
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name='设备'
		verbose_name_plural='设备'
		"""docstring for Meta"""
		def __init__(self, arg):
			super(Meta, self).__init__()
			self.arg = arg
			


'''
物资类
'''	
class Material(models.Model):
	#物资种类--------------------此处可以显示物料的编号：category.category_code
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='物资种类')
	#物资名称
	name =  models.CharField('物资名称', max_length=100)
	#规格型号
	model = models.CharField('规格型号', max_length=100)
	#单位
	unit = models.CharField('单位', max_length=100)
	#批号
	lot = models.CharField('批号', max_length=100)
	#生产日期
	production_date = models.DateField('生产日期')
	#到期日期
	expired_date = models.DateField('到期日期')
	#单价
	value = models.FloatField('单价')
	#生产厂家
	manufactor = models.CharField('生产厂家', max_length=100)
	#备注
	demo = models.TextField('备注')	
	
	class Meta:
		abstract = True
	
	

'''
单据类
'''	
class Receipe(models.Model):
	#业务类别
	type = models.CharField('业务类别', max_length=100)
	#单据日期
	receipe_date = models.DateField('单据日期')
	#单据编号
	receipe_number = models.CharField('单据编号', max_length=100)
	#出单人
	maker = models.CharField('出单人', max_length=100)
	
	class Meta:
		abstract = True



'''
入库单
'''	
class MaterialIn(Material, Receipe):	
	#供货商
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='供货商')	
	#采购人
	buyer = models.CharField('采购人', max_length=100)
	#仓库
	repository = models.CharField('仓库', max_length=100)
	#接收部门
	department = models.CharField('接收部门', max_length=100, default="后勤科")
	#数量
	quanlity = models.IntegerField('数量')		
	#摘要
	summary = models.CharField('备注', max_length=100)
	
	def __str__(self):
		return super.receipe_number
		
	class Meta(object):
		verbose_name='入库单'
		verbose_name_plural='入库单'

		
'''
出库单
'''
class MaterialOut(Material, Receipe):
	#对应的入库单
	materialIn = models.ForeignKey(MaterialIn, on_delete=models.CASCADE, verbose_name='对应入库单')
	#领用人
	user = models.CharField('领用人', max_length=100)
	#领用部门    
	department = models.CharField('领用科室', max_length=100)
	#用途
	usage = models.CharField('用途', max_length=100)
	#数量
	quanlity = models.CharField('数量', max_length=100)
	
	def __str__(self):
		return super.receipe_number

	class Meta:
		verbose_name='出库单'
		verbose_name_plural='出库单'
	
'''
申请单:
流程：申请者-》科长——》分管领导——》主管领导
流程追踪：
'''
class MaterialRequisition(models.Model):
	#标题
	title = models.CharField('标题', max_length=100)
	#申请者
	applicant = models.CharField('申请者', max_length=100, default="hanbin") 
	#科室
	department = models.CharField('科室', max_length=100, default="后勤科")
	#原因
	reson = models.TextField('原因', )
	#科长
	chief = models.CharField('科长', max_length=100, default="moufs")
	#分管领导
	charger = models.CharField('分管领导', max_length=100, default="scsh")
	#主管领导
	director = models.CharField('主管领导', max_length=100, default="yhl")
	
	def __str__(self):
		return self.title
	class Meta(object):
		verbose_name='申请单'
		verbose_name_plural='申请单'

			
	