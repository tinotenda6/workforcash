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
    path('savetask/', work_views.task, name='task-page'),
    path('alltasks/', work_views.alltasks, name='alltask-page'),
    path('indcl/<int:child_id>', work_views.indcl, name='indcl-page'),
    path('alltasks/<int:task_id>', work_views.update, name='update-page'),
    path('delete/<int:chore_id>/<str:task_name>/<int:child_id>', work_views.task_remove, name='task-remove'),
    path('deletetask/<int:task_id>', work_views.delete_task,name='complete-tdelete'),
    path('chores/', work_views.chorelist, name='chores-page'),
    path('pgname/', user_views.pgname, name='pgname-page'),
   #  path('pgconf/', user_views.pgconfirm, name='pgconf-page'),
    path('adm/', work_views.adm, name='adm-page'),
    path('register/child/', user_views.child_register, name='child-register'),
    path('register/pg/', user_views.pg_register, name='pg-register'),
    path('login/', user_views.login , name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login-page'), name='logout-page'),
]
