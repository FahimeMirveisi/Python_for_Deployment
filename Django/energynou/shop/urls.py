
from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    #path('products/', views.products, name='products'),
    #path('categories/', views.categories, name='categories'),
    path('product/<int:product_id>/', views.product, name='product'),
]