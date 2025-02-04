from django.forms import ModelForm, TextInput
from .models import UserCity

class CityForm(ModelForm):
    class Meta:
        model = UserCity
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
