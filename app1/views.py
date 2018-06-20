from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>hello benben<h2>')

from app1 import models       #导入blog模块
from django.shortcuts import HttpResponse

#def db_handle(request):
#    models.UserInfo.objects.create(username='andy',password='123456',age=33)
#   return HttpResponse('OK')

def db_handle(request):
    user_list_obj = models.UserInfo.objects.all()
    return render(request,'t1.html',{'li':user_list_obj})