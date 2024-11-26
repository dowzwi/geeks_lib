from django import forms

from basket.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone_number", "email", "book"]
