from django import forms
from apps.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'image_for_product', 'price']
