from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.settings import api_settings

from vocabs.filters import (
    SkosCollectionListFilter,
    SkosConceptListFilter,
    SkosConceptSchemeListFilter,
)
from vocabs.models import SkosCollection, SkosConcept, SkosConceptScheme
from vocabs.serializers import (
    SkosCollectionSerializer,
    SkosConceptSchemeSerializer,
    SkosConceptSerializer,
)


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 10000


class SkosConceptSchemeViewSet(viewsets.ModelViewSet):
    queryset = SkosConceptScheme.objects.all()
    serializer_class = SkosConceptSchemeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    pagination_class = LargeResultsSetPagination
    filter_class = SkosConceptSchemeListFilter


class SkosCollectionViewSet(viewsets.ModelViewSet):
    queryset = SkosCollection.objects.all()
    serializer_class = SkosCollectionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    pagination_class = LargeResultsSetPagination
    filter_class = SkosCollectionListFilter


class SkosConceptViewSet(viewsets.ModelViewSet):
    queryset = SkosConcept.objects.all()
    serializer_class = SkosConceptSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    pagination_class = LargeResultsSetPagination
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    filter_class = SkosConceptListFilter
