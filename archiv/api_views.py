# API views for archiv created by appcreator
import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework_gis.pagination import GeoJsonPagination


from archiv.api_serializers import (
    AutorSerializer,
    KeyWordSerializer,
    OrtSerializer,
    StelleSerializer,
    TextSerializer,
    SpatialCoverageSerializer,
    UseCaseSerializer
)
from archiv.models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase
)
from archiv.filters import (
    AutorListFilter,
    KeyWordListFilter,
    OrtListFilter,
    StelleListFilter,
    TextListFilter,
    SpatialCoverageListFilter,
    UseCaseListFilter
)


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = UseCaseListFilter


class SpatialCoverageViewSet(viewsets.ModelViewSet):
    queryset = SpatialCoverage.objects.all()
    serializer_class = SpatialCoverageSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = SpatialCoverageListFilter
    pagination_class = GeoJsonPagination


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = AutorListFilter


class KeyWordViewSet(viewsets.ModelViewSet):
    queryset = KeyWord.objects.all()
    serializer_class = KeyWordSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = KeyWordListFilter


class OrtViewSet(viewsets.ModelViewSet):
    queryset = Ort.objects.all()
    serializer_class = OrtSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = OrtListFilter


class StelleViewSet(viewsets.ModelViewSet):
    queryset = Stelle.objects.all()
    serializer_class = StelleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = StelleListFilter


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TextListFilter


# cut&paste the following snippet into your projects urls.py

# from archiv import api_views as archiv_api_views
# router.register(r'autor', archiv_api_views.AutorViewSet)
# router.register(r'edition', archiv_api_views.EditionViewSet)
# router.register(r'keyword', archiv_api_views.KeyWordViewSet)
# router.register(r'ort', archiv_api_views.OrtViewSet)
# router.register(r'stelle', archiv_api_views.StelleViewSet)
# router.register(r'text', archiv_api_views.TextViewSet)
