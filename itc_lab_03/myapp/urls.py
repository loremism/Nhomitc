from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:id>/', views.shop_single, name='shop_single'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
