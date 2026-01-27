
from django.urls import path
from . import views

urlpatterns=[
    path('all_products',views.all_products,name='all_products'),
    path('cart_data',views.cart_data,name='cart_data'),
   
]