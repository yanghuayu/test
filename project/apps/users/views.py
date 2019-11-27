# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re 
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from users.models import User
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.core.mail import send_mail
from django.http import HttpResponse
import redis
from django.conf import settings
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import check_password
from django_redis import get_redis_connection
# Create your views here.

class MeView(View):
	def get(self,request):
		return render(request,'me.html')

class RegisterView(View):
	def get(self,request):
		a=User.objects.get(username='qiuxiaoli')
		b=a.email
		print b
		return render(request,'register.html')
	def post(self,request):
		username=request.POST.get('username')
		pwd=request.POST.get('pwd')
		cpwd=request.POST.get('cpwd')
		email=request.POST.get('email')
		print username,pwd,cpwd,email
		if not all([username,pwd,cpwd,email]):
			return render(request,'register.html',{'error':'No wan zheng'})
		if cmp(pwd,cpwd):
			return render(request,'register.html',{'error':'No tong'})
		if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
			return render(request,'register.html',{'error':'邮箱格式错误'})
		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			user=None
		if user:
			return render(request,'register.html',{'error':'yi cunzai'})
		else:
			user=User.objects.create_user(username=username,password=pwd,email=email)
			user.is_active=0
			user.save()
		serializer=Serializer(settings.SECRET_KEY,3600)
		info={'confirm':user.id}
		token=serializer.dumps(info)
		token=token.decode('utf8')

		# subject='天天生鲜欢迎你'
		# message=''
		# html_message='<h1>%s,欢迎你成为天天生鲜会员</h1>请点击下面链接激活你的用户<br><a  href="http://192.168.0.199:8000/users/active/%s">http://192.168.0.199:8000/users/active/%s</a>'%(username,token,token)
		# sender=settings.EMAIL_FROM
		# receiver=[email]
		# send_mail(subject,message,sender,receiver,html_message=html_message)
		send_register_active_email.delay(email,username,token)#celery异步函数
		
		return redirect(reverse('goods:index'))


class ActiveView(View):
	def get(self,request,token):
		serializer=Serializer(settings.SECRET_KEY,3600)
		try:
			info = serializer.loads(token)
			user_id = info['confirm']
			user = User.objects.get(id=user_id)
			user.is_active = 1
			user.save()

			#跳转到登陆页面
			return redirect(reverse('users:login'))
		except SignatureExpired as e:
			#激活已过期	
			return HttpResponse('激活已过期')

class LoginView(View):
	def get(self,request):
		# print 'ppp'
		# con=redis.Redis(host='127.0.0.1',port=6379,db=6)
		con=get_redis_connection("session")
		con.set('laowang','shui')
		con.hset('xx','laowang','shi ni')
		val=con.get('laowang')
		val2=con.hget('xx','laowang')
		print val,val2
		if 'username' in request.COOKIES:
			username=request.COOKIES.get('username')
			checked='checked'
		else:
			username=''
			checked=''
		return render(request,'login.html',{'username':username,'checked':checked})

	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username,password
		if not all([username,password]):
			print 1
			return render(request,'login.html',{'errmsg':'shujv mei tianxue'})
		try:
			
			user0=User.objects.get(username=username)
			print 'cun zai '
		except User.DoesNotExist:
			print 'user dos not'
			user0=None

		user = authenticate(username=username,password=password)
		print user,type(user)

		if user is not None and check_password(password,user.password):
			if user.is_active:
				print 'ok'
				login(request,user)
				request.session.set_expiry(None)
				print 66
				return redirect(reverse('goods:index'))
			
			else:
				print 2
				return render(request,'login.html',{'errmsg':'please active'})
		else:
			print 3
			return render(request,'login.html',{'errmsg':'mima huo username cuo wu'})

#/user/logout
class LogoutView(View):#退出用户
	def get(self,request):
		logout(request)#退出函数
		return redirect(reverse('goods:index'))