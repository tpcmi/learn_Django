from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('myapp/show',views.show_users,name='show'),
    path('myapp/add',views.add_users,name='add_users'),
    path('myapp/insert',views.insert_users,name='insert_users'),
    path('myapp/del/<int:uid>',views.del_users,name='del_users'),
    path('myapp/edit/<int:uid>',views.edit_users,name='edit_users'),
    path('myapp/update',views.update_users,name='update_users'),
]