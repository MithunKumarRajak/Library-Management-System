from django.urls import path
from .views import RegisterView, LoginView, Dashboard

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
