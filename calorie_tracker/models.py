# calorie_tracker/models.py

from django.db import models
from datetime import date

class FoodItem(models.Model):
    """
    Model to store individual food items consumed by the user, 
    along with their calorie count and the date they were consumed.
    """
    # Name of the food item (e.g., 'Apple', 'Sandwich')
    name = models.CharField(max_length=100)
    
    # Calorie count (must be a non-negative integer)
    calories = models.IntegerField(default=0)
    
    # Date the food was consumed (defaults to today)
    date_consumed = models.DateField(default=date.today)

    def __str__(self):
        """Returns a string representation of the food item."""
        return f"{self.name} ({self.calories} cal on {self.date_consumed})"
    
    class Meta:
        # Order items by date (newest first) and then by ID
        ordering = ['-date_consumed', '-id']