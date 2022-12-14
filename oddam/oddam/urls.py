"""oddam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from oddam_app.views import (IndexView, LoginView, AddDonationView, RegisterView,
                             LogoutView, UserDetailsView, PasswordBeforeSettings, ChangeUserSettingsView)



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_donation/', AddDonationView.as_view(), name='add_donation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_details/<int:id>', UserDetailsView.as_view(), name='user_details'),
    path('password_check/', PasswordBeforeSettings.as_view(), name='password_check'),
    path('change_user_settings/', ChangeUserSettingsView.as_view(), name='change_user_settings'),
]
