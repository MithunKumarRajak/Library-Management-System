"""
URL configuration for LibraryManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import RegisterView, LoginView, Dashboard
from maps.views import map_view
# Import the send_test_email view
from .views import email_page, send_test_email
# JWT Views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Custom 404 handler
handler404 = 'LibraryManagementSystem.views.handler404'

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # App routes
    path('', include('books.urls')),
    path('noticeboard/', include('noticeBoard.urls')),
    path('api/', include('accounts.urls')),

    # Authentication (JWT)
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Dashboard
    path('api/dashboard/', Dashboard.as_view(), name='dashboard'),

    # Map
    path('map/', map_view, name='map'),

    # Test email
    path('email/', email_page, name='email_page'),
    path('send-email/', send_test_email, name='send_test_email'),
    # Home for message form
    path ('home/', include('home.urls')),    
]
