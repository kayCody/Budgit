from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('contact_us/', views.contact, name='contact'),
    path('successfull/', views.success, name='success'),
    path('search/',views.search, name="search" )
]