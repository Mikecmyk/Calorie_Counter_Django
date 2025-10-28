# calorie_tracker/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm
from datetime import date

def index(request):
    """
    Handles displaying the main dashboard, adding new food items, 
    and resetting the daily calorie count.
    (Covers Read, Create, and Reset Functionality)
    """
    # 1. READ & CALCULATION SETUP
    today = date.today()
    food_items = FoodItem.objects.filter(date_consumed=today)
    
    # Calculate total calories consumed for the day
    total_calories = sum(item.calories for item in food_items)
    
    form = FoodItemForm()

    # 2. CREATE (Add Food Item) & RESET LOGIC
    if request.method == 'POST':
        # Check if the user clicked the 'add_food' button
        if 'add_food' in request.POST:
            form = FoodItemForm(request.POST)
            if form.is_valid():
                # Saves the new FoodItem with today's date (due to model default)
                form.save()
                # Redirect to the same page to show the updated list (PRG pattern)
                return redirect('index') 
        
        # Check if the user clicked the 'reset_day' button
        elif 'reset_day' in request.POST:
            # Delete all FoodItems logged for today
            FoodItem.objects.filter(date_consumed=today).delete()
            return redirect('index')
            
    # Context to pass data to the HTML template
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
        'form': form,
        'today': today.strftime("%A, %B %d, %Y")
    }
    return render(request, 'calorie_tracker/index.html', context)


def remove_food(request, item_id):
    """
    Handles the deletion of a specific food item by its ID.
    (Covers Delete Functionality)
    """
    # Get the item or return a 404 error if not found
    item = get_object_or_404(FoodItem, id=item_id)
    
    if request.method == 'POST':
        item.delete()
        # Redirect back to the main page after deletion
        return redirect('index')
        
    # If someone tries to access this via GET, just redirect them back
    return redirect('index')