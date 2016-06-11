from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):

    """Docstring for EventSerializer. Serializer for the Event, which need's
    to return and represent model fields.
    """

    def to_representation(self, obj):
        """TODO: to be defined1. """
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'date': obj.date,
            'image': obj.image,
        }

    class Meta:
        model = Event
        fields = ('name', 'description', 'date', 'image',)
