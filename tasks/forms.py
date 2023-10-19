from django import forms
from .models import IceCream

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'description', 'price']
        labels = {
            'flavor': 'Вкус мороженого',
            'description': 'Описание мороженого',
            'price': 'Цена',
        }
