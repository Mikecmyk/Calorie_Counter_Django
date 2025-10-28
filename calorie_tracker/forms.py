# calorie_tracker/forms.py (CREATE THIS NEW FILE)

from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    """
    A form based on the FoodItem model for adding new calorie entries.
    """
    class Meta:
        model = FoodItem
        # Only expose name and calories to the user
        fields = ['name', 'calories'] 
        
        # Add basic HTML attributes for better usability and Tailwind styling compatibility
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Apple, Salad', 'class': 'w-full px-3 py-2 border rounded-lg'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'e.g., 95', 'class': 'w-full px-3 py-2 border rounded-lg', 'min': 0}),
        }