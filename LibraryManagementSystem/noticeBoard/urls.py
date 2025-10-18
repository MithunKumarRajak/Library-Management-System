from django.urls import path, include
from noticeBoard.views import notice

urlpatterns = [
    path('', notice, name='notice'),
]
