from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Event
from .serializers import EventSerializer


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(status="open").select_related(
        "venue"
    )  # select_related для предотвращения N+1
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["event_time"]
    ordering = ["event_time"]
    pagination_class = None
