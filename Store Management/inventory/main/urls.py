from django.urls import path

from . import  views

app_name = 'main'

urlpatterns = [
    path('',views.homepage , name ='homepage'),
    path('all_products' ,views.show_all_products, name = 'all_products'),
    path('sell_history' ,views.sell_history, name = 'sell_history'),
    path('purchase_history' ,views.purchase_history, name = 'purchase_history'),


]