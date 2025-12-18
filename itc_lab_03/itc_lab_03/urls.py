"""
URL configuration for itc_lab_03 project.

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
from django.urls import path
from myapp import views
urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
=======
    path('', views.index, name='home'),
>>>>>>> e139c0d27c8a1c77d5f0abf76877e21ae1a2af65
    path('admin/', admin.site.urls),
]
