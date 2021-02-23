
from django.urls import path
from .views import index,login,signup,store,logout,orders,product,cart,checkout

urlpatterns = [
  path('',index),
  path('login',login,name='login'),
  path('logout',logout,name='logout'),
  path('signup',signup,name='signup'),
  path('store',store,name='store'),
  path('orders',orders,name='orders'),
  path('cart',cart,name='cart'),
  path('product',product,name='product'),
  path('checkout',checkout,name='checkout')
]