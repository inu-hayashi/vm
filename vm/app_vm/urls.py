from django.urls import path
from . import views

app_name = 'app_vm'
urlpatterns = [
    path('', views.index, name='index'),
    path('kirin',views.kirin, name ='kirin')
]