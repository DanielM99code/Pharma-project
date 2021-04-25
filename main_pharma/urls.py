from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [

    path('', main_page_view, name='main_page_view'),
    path('shop/', shop_page_view, name='shop_page_view'),
    path('shop/<slug:slug>', prod_page_view, name='prod_page_view'),
    path('about/', about_page_view, name='about_page_view'),
    path('contact_us/', contact_us_page_view, name='contact_us_page_view'),
    path('search/', search_product, name='search')


]
