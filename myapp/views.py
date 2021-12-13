from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import MyappUsers
from datetime import datetime
import django
# Create your views here.

def index(request):
    
    mod = MyappUsers.objects
    ulist = mod.filter(age__gte=20)
    for u in ulist:
        print(u.id,u.name,u.age,u.phone)
    return HttpResponse("First Page.")
    
def show_users(request):
    # try:
    ulist = MyappUsers.objects.all()
    context = {'userlist':ulist}
    return render(request,'myapp/index.html',context)
    # except:
    #     return HttpResponse('数据读取错误！')

def add_users(request):
    pass

def insert_users(request):
    pass

def del_users(request,uid=0):
    pass

def edit_users(request,edit=0):
    pass

def update_users(request):
    pass

    