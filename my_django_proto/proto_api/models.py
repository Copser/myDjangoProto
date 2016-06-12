from django.db import models
import datetime

# Create your models here.


class ContactUsForm(models.Model):

    """Docstring for ContactUs. """
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    topic = models.CharField(max_length=250)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        """TODO: to be defined1. """
        return self.email

    class Meta:
        ordering = ['-timestamp']
