from django import forms
from rent.models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'