from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'Bprice', 'Sprice', 'image', 'amount', 'category', 'subcategory']
        labels = {
            'Sprice': 'Selling Price',
            'Bprice': 'Buying Price',
            'amount': 'Quantity'
        }