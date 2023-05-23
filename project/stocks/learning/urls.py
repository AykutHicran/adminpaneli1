from django.urls import path
from . import views

# learning url yi buraya yazacagim


urlpatterns = [
    path('product/', views.products),
    path('product/detail/<int:pk>/', views.product),
    path('product/archieve/', views.product_archieve),
    
]