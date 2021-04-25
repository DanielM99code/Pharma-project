from django.urls import path, include
from .views import *

urlpatterns = [

    path('', main_admin_view, name='main_admin_view'),
    path('messages/', list_of_messages, name='list_of_messages'),
    path('messages/update/<int:pk>', update_message, name='update_message'),

    path('products/', list_of_products, name='list_of_products'),
    path('products/add/', ProductAddView.as_view(), name='products_add'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='products_delete'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='products_update'),

    path('categories/', list_of_categories, name='list_of_categories'),
    path('categories/add', CategoryAddView.as_view(), name='categories_add'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='categories_delete'),
    path('categories/update/<int:pk>', CategoryUpdateView.as_view(), name='categories_update'),

    path('orders/', list_of_orders, name='list_of_orders')

]
