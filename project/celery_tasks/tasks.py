#coding=utf8
from django.core.mail import send_mail
from celery import Celery
from django.conf import settings 

from django.template import loader,RequestContext#django自带的静态网页生成器
# from django_redis import get_redis_connection
import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
django.setup()

from goods.models import *


app = Celery('celery_tasks.tasks',broker='redis://:as910329@192.168.0.199:6379/2') 

@app.task
def send_register_active_email(to_email,username,token):
	subject = '天天生鲜欢迎你'
	message = ''
	html_message ='<h1>%s,欢迎你成为天天生鲜会员</h1>请点击下面链接激活你的用户<br><a href="http://192.168.0.199:8000/users/active/%s">http://192.168.0.199:8000/users/active/%s</a>'%(username,token,token)
	sender = settings.EMAIL_FROM
	receiver = [to_email]
	send_mail(subject,message,sender,receiver,html_message=html_message)

