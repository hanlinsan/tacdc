from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Supplier


# Create your views here.
def index(request):
	return HttpResponse("hello, you are in HQK")
	
def supplierDetail(request, supplier_id):
	return HttpResponse("You're looking at supplier's detail:")
	
def supplier_list(request):
	supplier_list = Supplier.objects.order_by('company_name')
	template = loader.get_template('base.html')
	context = {'all_supplier_list':supplier_list}
	return HttpResponse(template.render(context, request))