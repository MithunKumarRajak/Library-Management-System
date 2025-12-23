from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manual/', views.message_manual, name='message_manual'),
    path('form/', views.message_form, name='message_form'),
    path('modelform/', views.message_modelform, name='message_modelform'),
]
