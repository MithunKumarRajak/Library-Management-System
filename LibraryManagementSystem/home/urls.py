from django.urls import path
from home.views import message_view

urlpatterns = [
    path('', message_view, name='message'),
]
