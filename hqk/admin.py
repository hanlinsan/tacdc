from django.contrib import admin
from .models import Supplier, Category, Device, MaterialIn, MaterialOut, MaterialRequisition
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Device)
admin.site.register(Category)
admin.site.register(MaterialIn)
admin.site.register(MaterialOut)
admin.site.register(MaterialRequisition)
