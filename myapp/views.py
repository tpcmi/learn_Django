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
    pass

def add_users(request):
    pass

def insert_users(request):
    pass

def del_users(request):
    pass

def edit_users(request):
    pass

    