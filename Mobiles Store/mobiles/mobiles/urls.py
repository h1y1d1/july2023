"""mobiles URL Configuration

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
from mobile_app.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home"),
    path('samsung/',samsung, name="samsung"),
    path('vivo/',vivo, name="vivo"),
    path('redmi/',redmi, name="redmi"),
    path('oppo/', oppo, name="oppo"),
    path('realme/',realme, name="realme"),
    path('honor/', honor,name="honor"),
    path('oneplus/', oneplus,name="oneplus"),
    path('iqoo/', iqoo,name="iqoo"),
    path('poco/', poco,name="poco"),
    path('lenovo/', lenovo,name="lenovo"),
    path('huawei/', huawei,name="huawei"),
    path('nokia/', nokia,name="nokia"),
    path('products/',products ,name="products"),
    path("",login_user,name="login"),
    path("register/",register,name="register"),
    path("logout/",logout_user,name="logout"),
    path("contact/",contact,name="contact"),
    
]

