from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):

    """Docstring for EventViewSet. Basically this ViewSet will when a request come it call
    get_queryset to get a queryset, and that is what it needs to return. It can be seen as an
    array of instances of the Event model. You don't just want to return events for events/,
    rather then you want to be able when you type events/1 to return all events for that special
    id, so when type /events/1 and it will return for that id(pk(primary key)).
    """
    serializer_class = EventSerializer

    def get_queryset(self,):
        """TODO: to be defined1. """
        queryset = Event.objects.all()
        uid = self.kwargs.get('pk')
        if uid:
            return queryset.filter(pk=uid)
        else:
            return queryset
