from django.forms import ModelForm
from .models import ContactUsForm
from django import forms


class ContactUsView(ModelForm):

    """Docstring for ContactUsView. """
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['name', 'email', 'topic', 'message']
        model = ContactUsForm
