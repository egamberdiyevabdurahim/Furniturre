from django import forms

from products.models import ColorModel


class ColorPickerForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = ['code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'}),
        }
