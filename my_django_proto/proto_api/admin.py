from django.contrib import admin
from .models import ContactUsForm

# Register your models here.


class ContactUsFormAdmin(admin.ModelAdmin):

    """Docstring for ContactUsFormAdmin. """
    class Meta:
        model = ContactUsForm

admin.site.register(ContactUsForm, ContactUsFormAdmin)
