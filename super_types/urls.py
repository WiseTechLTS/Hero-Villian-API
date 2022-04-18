from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_types_list),
    path('127.0.0.1:8000/api/supers/<int:pk>/', views.super_types_detail),
]