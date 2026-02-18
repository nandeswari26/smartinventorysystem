from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Sale


# ===================== PRODUCT FORM =====================
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'category',
            'supplier',
            'price',
            'current_stock',
            'reorder_level'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter SKU'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'supplier': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter supplier name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01'
            }),
            'current_stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'reorder_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price

    def clean_current_stock(self):
        stock = self.cleaned_data.get('current_stock')
        if stock is None or stock < 0:
            raise ValidationError("Stock cannot be negative.")
        return stock

    def clean_reorder_level(self):
        reorder = self.cleaned_data.get('reorder_level')
        if reorder is None or reorder < 0:
            raise ValidationError("Reorder level cannot be negative.")
        return reorder

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')

        if Product.objects.filter(sku=sku).exclude(pk=self.instance.pk).exists():
            raise ValidationError("SKU must be unique.")

        return sku


# ===================== SALE FORM =====================
class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold']

        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control'
            }),
            'quantity_sold': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }

    def clean_quantity_sold(self):
        quantity = self.cleaned_data.get('quantity_sold')

        if quantity is None or quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

        return quantity
