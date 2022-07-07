from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path as url


urlpatterns = [
    path('',views.Main, name="Main"),
    path('about/',views.About, name="About"),
    path('admin/', admin.site.urls),
    path('menu/',views.Menu, name="Menu"),
    path('order/',views.OrderPage, name="Order"),
    path('review/',views.Review, name="Review"),
    path('contact/',views.Contact, name="Contact"),
    path('cart/',views.CartItems, name="Cart"),
    path('adminlogin/',views.AdminLogin, name="AdminLogin"),
    path('adminproduct/',views.AdminProduct, name="AdminProduct"),
    path('admincustomer/',views.AdminCustomer, name="AdminCustomer"),
    path('adminorder/',views.AdminOrder, name="AdminOrder"),
    path('createproduct/',views.createProduct, name="createProduct"),
    path('updateproduct/<str:pk>/',views.updateProduct, name="updateProduct"),
    path('deleteproduct/<str:pk>/',views.deleteProduct, name="deleteProduct"),
    path('updatecustomer/<str:pk>/',views.updateCustomer, name="updateCustomer"),
    path('deletecustomer/<str:pk>/',views.deleteCustomer, name="deleteCustomer"),
    path('updateorder/<str:pk>/',views.updateOrder, name="updateOrder"),
    path('deleteorder/<str:pk>/',views.deleteOrder, name="deleteOrder"),


]
