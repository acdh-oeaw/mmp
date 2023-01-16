# API views for archiv created by appcreator
import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination


from archiv.api_serializers import (
    AutorSerializer,
    KeyWordSerializer,
    OrtSerializer,
    StelleSerializer,
    TextSerializer,
    SpatialCoverageSerializer,
    SpatialCoverageGroupSerializer,
    UseCaseSerializer,
    ConeSerializer,
    GeoJsonOrtSerializer,
    FuzzyGeoJsonOrtSerializer,
    StorySerializer,
    SlideSerializer,
    EventSerializer
)
from archiv.models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase,
    Event
)
from archiv.filters import (
    AutorListFilter,
    KeyWordListFilter,
    OrtListFilter,
    StelleListFilter,
    TextListFilter,
    SpatialCoverageListFilter,
    UseCaseListFilter,
    EventListFilter
)

from story_map.models import Story, Slide


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().distinct()
    serializer_class = StorySerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all().distinct()
    serializer_class = SlideSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.filter(published=True).distinct()
    serializer_class = UseCaseSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = UseCaseListFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().distinct()
    serializer_class = EventSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = EventListFilter


class SpatialCoverageViewSet(viewsets.ModelViewSet):
    queryset = SpatialCoverage.objects.exclude(fuzzy_geom=None).distinct()
    serializer_class = SpatialCoverageSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = SpatialCoverageListFilter
    pagination_class = GeoJsonPagination


class SpatialCoverageGroupViewSet(viewsets.ModelViewSet):
    queryset = SpatialCoverage.objects.exclude(geom_collection__isnull=True).distinct()
    serializer_class = SpatialCoverageGroupSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = SpatialCoverageListFilter
    pagination_class = GeoJsonPagination


class ConeViewSet(viewsets.ModelViewSet):
    queryset = SpatialCoverage.objects.exclude(fuzzy_geom=None)\
        .exclude(stelle__text__ort__isnull=True).distinct()
    serializer_class = ConeSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = SpatialCoverageListFilter
    pagination_class = GeoJsonPagination


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().distinct()
    serializer_class = AutorSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = AutorListFilter


class KeyWordViewSet(viewsets.ModelViewSet):
    queryset = KeyWord.objects.all().distinct()
    serializer_class = KeyWordSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = KeyWordListFilter


class OrtViewSet(viewsets.ModelViewSet):
    queryset = Ort.objects.all().distinct()
    serializer_class = OrtSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = OrtListFilter


class GeoJsonOrtViewSet(viewsets.ModelViewSet):
    queryset = Ort.objects.exclude(coords__isnull=True).distinct()
    serializer_class = GeoJsonOrtSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = OrtListFilter
    pagination_class = GeoJsonPagination


class FuzzyGeoJsonOrtViewSet(viewsets.ModelViewSet):
    queryset = Ort.objects.exclude(fuzzy_geom__isnull=True).distinct()
    serializer_class = FuzzyGeoJsonOrtSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = OrtListFilter
    pagination_class = GeoJsonPagination


class StelleViewSet(viewsets.ModelViewSet):
    queryset = Stelle.objects.all().distinct()
    serializer_class = StelleSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = StelleListFilter


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all().distinct()
    serializer_class = TextSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        OrderingFilter
    ]
    filter_class = TextListFilter


# cut&paste the following snippet into your projects urls.py

# from archiv import api_views as archiv_api_views
# router.register(r'autor', archiv_api_views.AutorViewSet)
# router.register(r'edition', archiv_api_views.EditionViewSet)
# router.register(r'keyword', archiv_api_views.KeyWordViewSet)
# router.register(r'ort', archiv_api_views.OrtViewSet)
# router.register(r'stelle', archiv_api_views.StelleViewSet)
# router.register(r'text', archiv_api_views.TextViewSet)
