"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin

from . import view
# from jceApp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('admin/hello', view.hello)
    url(r'^$', view.home),
    url(r'^route1$', view.route1),
    url(r'^newIndex$', view.newIndex),
    url(r'^getCoreData$', view.getCoreData),
    # url(r'^createSubscriber$', jce.createSubscriber),
    # url(r'^jceApp/homepage', homePage) ,
    url(r'^jceApp/', include("jceApp.urls")),
]
