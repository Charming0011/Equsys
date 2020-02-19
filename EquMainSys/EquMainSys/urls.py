"""EquMainSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from equipment import views,login_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login_views.user_login),
    path('stulogin/', login_views.stu_login),
    path('index/', views.index),
    path('logout/', login_views.user_logout),
    path('submaninfo/', login_views.submaninfo),
    path('subadd/', login_views.subadd),
    # path('stulogout/', login_views.stu_logout),


    path('index/', include('equipment.urls')),
]