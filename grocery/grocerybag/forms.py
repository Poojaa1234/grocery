from .models import Grocery
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


STATUS_CHOICES = (
    ('PENDING','pending'),
    ('BOUGHT', 'bought'),
    ('NOT AVAILABLE','not available'),
)

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Item Name'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control','placeholder':'Item Quantity'}),
            'date':DateInput(attrs={'class':'form-control'}),
        }