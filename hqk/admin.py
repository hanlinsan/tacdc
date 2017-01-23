
from django.contrib import admin
from .models import Supplier, Category, Device, MaterialIn, MaterialOut, MaterialRequisition


# Register your models here.

admin.site.register(Supplier)
admin.site.register(Device)
admin.site.register(Category)


#入库单
class MaterialInAdmin(admin.ModelAdmin):
	fieldsets = (
		('基本信息：', {'fields':(('receipe_number', 'receipe_date', 'type'), ('supplier', 'repository', 'buyer')), 'classes':('wide', 'extrapretty')}),
		('物资基本信息：', {'fields':(('category', 'name', 'model', 'value'),('unit', 'lot', 'production_date', 'expired_date'),('manufactor', 'demo'))}),
	)
admin.site.register(MaterialIn, MaterialInAdmin)
#入库单后台管理结束


admin.site.register(MaterialOut)

admin.site.register(MaterialRequisition)
