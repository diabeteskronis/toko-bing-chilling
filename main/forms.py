from django.forms import ModelForm
from main.models import Product

class IceCreamEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "icecreamrating"]