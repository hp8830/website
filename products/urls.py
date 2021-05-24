from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('trending/', views.trending),
    path('clearance/', views.clearance)
] 