from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('<str:city>/', views.city_detail)
]