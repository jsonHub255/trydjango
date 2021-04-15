from os import name
from django.urls import path
from .views import *


app_name = 'products'
urlpatterns = [
    path('', procuct_list_view, name="product_list_view"),
    path('<int:id>/', product_dynamic_view, name="product_dynamic_view"),
    path('create/', product_create_view, name="product_create_view"),
    path('update/<int:id>/', update_product, name="intial_update_datas"),
    path('<int:id>/delete/', product_delete_view, name="delete_product")
]
