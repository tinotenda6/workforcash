"""WFYM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users import views as user_views
from work import views as work_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('chhome/', work_views.chhome, name='chhome-page'),
    path('pghome/', work_views.pghome, name='pghome-page'),
    path('adm/', work_views.adm, name='adm-page'),
    path('register/child/', user_views.child_register, name='child-register'),
    path('register/pg/', user_views.pg_register, name='pg-register'),
    path('login/', user_views.login , name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login-page'), name='logout-page'),
]
