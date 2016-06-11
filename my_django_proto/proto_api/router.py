from rest_framework import routers
from .events.views import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet, base_name='event')
