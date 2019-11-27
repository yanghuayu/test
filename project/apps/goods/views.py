# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import GoodsType,GoodsSKU,Goods,IndexGoodsBanner
from django.core.cache import cache#缓存（redis作为缓存）

# Create your views here.
# def index(request):
# 	return render(request,'index.html')

class IndexView(View):
	def get(self,request):
		context=cache.get("index_page_data")
		if context is None:
			types=GoodsType.objects.all()
			skus=GoodsSKU.objects.all()
			context={
			'types':types,
			'skus':skus
			}
			cache.set('index_page_data',context,36)
		user=request.user
		if user.is_authenticated():
			print 'logined'
		else:
			return render(request,'login.html')
		return render(request,'index.html',context)

class CategoryView(View):
	def get(self,request):
		types=GoodsType.objects.all().exclude(logo='1')
		skus=GoodsSKU.objects.all()
		context={
			'types':types,
			'skus':skus
		}
		user=request.user
		if user.is_authenticated():
			print 'logined'
		else:
			return render(request,'login.html')

		return render(request,'category.html',context)



class SearchView(View):
	def get(self,request):
		return render(request,'search.html')




class DetailView(View):
	def get(self,request,goods_id):
		return render(request,'detail.html')



