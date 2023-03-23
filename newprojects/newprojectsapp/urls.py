from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('add/',views.operation,name='addition'),
    #path('sub/',views.operation,name='subtraction'),
    #path('mul/',views.operation,name='multiplication'),
    #path('div/',views.operation,name='division')
]
