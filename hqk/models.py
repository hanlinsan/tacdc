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
	company_name = models.CharField(max_length=100)
	# 业务种类
	#categories = models.TextField()
	# 联系人
	contactor = models.CharField(max_length=100)
	# 电话
	phone = models.CharField(max_length=100)
	# 邮箱
	email = models.EmailField()
	# 公司电话，或者传真
	company_phone = models.CharField(max_length=100)
	# 地址
	address = models.CharField(max_length=254)
	# 附件，例如：营业执照等
	attachments = models.FileField(upload_to='./uploads/%Y/%m/%d/')
	# 评价等级
	evaluation = models.CharField(max_length=100)
	# 摘要
	summary = models.TextField()
	
	def __str__(self):
		return self.company_name
	
	
class Category(models.Model):
	# 种类名称
	category_name = models.CharField(max_length=100)
	# 类别代码，设备，生活用品等分类
	category_code = models.IntegerField()
	# 供应商可以提供多个种类服务，因此是多对多的关系
	suppliers = models.ManyToManyField(Supplier)
	# 摘要
	summary = models.TextField()
	
	def __str__(self):
		return self.category_name

	
	
class Device(models.Model):
	# 唯一性编号
	number = models.CharField(max_length=100)
	# 设备类型，-----------外键
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# 设备名称
	name = models.CharField(max_length=100)
	# 规格型号
	model = models.CharField(max_length=100)
	# 出厂编号
	factory_id = models.CharField(max_length=100)
	# 参数
	parameters = models.TextField()
	# 生产厂家
	manufactor = models.CharField(max_length=100)
	# 出厂日期
	release_date = models.DateField()
	# 购置日期
	acquisition_date = models.DateField()
	# 启用日期
	received_date = models.DateField()
	# 使用科室
	department = models.CharField(max_length=100)
	# 保管人
	keeper = models.CharField(max_length=100)
	# 价值
	value = models.FloatField()
	# 供应商,---------------外键 设备与供应商的关系是多对一的关系
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	# 备注
	demo = models.TextField()
	
	def __str__(self):
		return self.name


'''
物资类
'''	
class Material(models.Model):
	#物资种类
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	#物资名称
	name =  models.CharField(max_length=100)
	#规格型号
	model = models.CharField(max_length=100)
	#单位
	unit = models.CharField(max_length=100)
	#批号
	lot = models.CharField(max_length=100)
	#生产日期
	production_date = models.DateField()
	#到期日期
	expired_date = models.DateField()
	#单价
	value = models.FloatField()
	#生产厂家
	manufactor = models.CharField(max_length=100)
	#备注
	demo = models.TextField()	
	
	class Meta:
		abstract = True
	
	

'''
单据类
'''	
class Receipe(models.Model):
	#业务类别
	type = models.CharField(max_length=100)
	#单据日期
	receipe_date = models.DateField()
	#单据编号
	receipe_number = models.CharField(max_length=100)
	#出单人
	maker = models.CharField(max_length=100)
	
	class Meta:
		abstract = True



'''
入库单
'''	
class MaterialIn(Material, Receipe):	
	#供货商
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)	
	#采购人
	buyer = models.CharField(max_length=100)
	#仓库
	repository = models.CharField(max_length=100)
	#部门
	department = models.CharField(max_length=100, default="hqk")
	#数量
	quanlity = models.IntegerField()		
	#摘要
	summary = models.CharField(max_length=100)
	
	def __str__(self):
		return super.receipe_number

		
'''
出库单
'''
class MaterialOut(Material, Receipe):
	#对应的入库单
	materialIn = models.ForeignKey(MaterialIn)
	#领用人
	user = models.CharField(max_length=100)
	#领用部门    
	department = models.CharField(max_length=100)
	#用途
	usage = models.CharField(max_length=100)
	#数量
	quanlity = models.CharField(max_length=100)
	
	def __str__(self):
		return super.receipe_number
	
	
'''
申请单:
流程：申请者-》科长——》分管领导——》主管领导
流程追踪：
'''
class MaterialRequisition(models.Model):
	#标题
	title = models.CharField(max_length=100)
	#申请者
	applicant = models.CharField(max_length=100, default="hanbin") 
	#科室
	department = models.CharField(max_length=100, default="hqk")
	#原因
	reson = models.TextField()
	#科长
	chief = models.CharField(max_length=100, default="moufs")
	#分管领导
	charger = models.CharField(max_length=100, default="scsh")
	#主管领导
	director = models.CharField(max_length=100, default="yhl")
	
	def __str__(self):
		return self.title
	