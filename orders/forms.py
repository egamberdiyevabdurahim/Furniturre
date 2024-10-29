from django import forms

from orders import models


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.OrderModel
        fields = ['full_name', 'phone_number', 'email']
