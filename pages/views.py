from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'pages/contact.html'



