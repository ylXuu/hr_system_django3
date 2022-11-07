from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register_confirm/', views.register_confirm, name='register_confirm'),
    path('forget/', views.forget, name='forget'),
    path('worker/', views.worker, name='worker'),
    path('worker_query/', views.worker_query, name='worker_query'),
    path('worker_add/', views.worker_add, name='worker_add'),
    path('worker_add_confirm/', views.worker_add_confirm, name='worker_add_confirm'),
    url(r'worker_modify/(\d+)', views.worker_modify, name='worker_modify'),
    url(r'worker_delete/(\d+)', views.worker_delete, name='worker_delete'),
    path('department/', views.department, name='department'),
    path('training/', views.training, name='training'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('salary/', views.salary, name='salary'),
    path('reward/', views.reward, name='reward'),
    path('account/', views.account, name='account'),
]
