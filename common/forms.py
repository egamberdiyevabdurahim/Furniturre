from django import forms

from common.models import ContactUsModel


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'subject', 'message']
