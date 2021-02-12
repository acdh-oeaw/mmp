# API views for archiv created by appcreator
from rest_framework import viewsets

from archiv.api_serializers import (
    AutorSerializer,
    EditionSerializer,
    KeyWordSerializer,
    OrtSerializer,
    StelleSerializer,
    TextSerializer
)
from archiv.models import (
    Autor,
    Edition,
    KeyWord,
    Ort,
    Stelle,
    Text
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    depth = 2


class EditionViewSet(viewsets.ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    depth = 2


class KeyWordViewSet(viewsets.ModelViewSet):
    queryset = KeyWord.objects.all()
    serializer_class = KeyWordSerializer
    depth = 2


class OrtViewSet(viewsets.ModelViewSet):
    queryset = Ort.objects.all()
    serializer_class = OrtSerializer
    depth = 2


class StelleViewSet(viewsets.ModelViewSet):
    queryset = Stelle.objects.all()
    serializer_class = StelleSerializer
    depth = 2


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    depth = 2




# cut&paste the following snippet into your projects urls.py

# from archiv import api_views as archiv_api_views
# router.register(r'autor', archiv_api_views.AutorViewSet)
# router.register(r'edition', archiv_api_views.EditionViewSet)
# router.register(r'keyword', archiv_api_views.KeyWordViewSet)
# router.register(r'ort', archiv_api_views.OrtViewSet)
# router.register(r'stelle', archiv_api_views.StelleViewSet)
# router.register(r'text', archiv_api_views.TextViewSet)
