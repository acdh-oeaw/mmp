import django_filters.rest_framework
from rest_framework import viewsets

from .api_serializer import GeoJsonLayerSerializer
from .models import GeoJsonLayer


class GeoJsonLayerViewSet(viewsets.ModelViewSet):
    queryset = GeoJsonLayer.objects.all().distinct()
    serializer_class = GeoJsonLayerSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_fields = [
        "use_case",
    ]
