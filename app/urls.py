from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('category/', views.category, name="category"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('checkout/shipping_address/', views.shipping_address_view, name='shipping_address'),


]
