# calorie_counter_project/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include calorie_tracker app URLs at the root path ''
    path('', include('calorie_tracker.urls')), 
]