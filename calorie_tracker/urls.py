# calorie_tracker/urls.py (CREATE THIS FILE)

from django.urls import path
from . import views

urlpatterns = [
    # C/R/Reset: Main page - Handles viewing, adding (POST), and resetting (POST)
    path('', views.index, name='index'), 
    
    # D: Remove food item (using a primary key 'item_id')
    path('remove/<int:item_id>/', views.remove_food, name='remove_food'),
]