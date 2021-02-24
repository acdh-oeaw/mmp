# API serializers for archiv created by appcreator
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from archiv.models import (
    Autor,
    Edition,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage
)


class SpatialCoverageSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):

    text_title = serializers.CharField(source='stelle.text.title')
    text_author = serializers.CharField(source='stelle.text.autor')

    class Meta:
        model = SpatialCoverage
        geo_field = 'fuzzy_geom'
        auto_bbox = True
        fields = (
            'text_title',
            'text_author',
            'stelle',
            'key_word'
        )


class AutorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Autor
        fields = "__all__"


class EditionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Edition
        fields = "__all__"


class KeyWordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = KeyWord
        fields = "__all__"


class OrtSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ort
        fields = "__all__"


class StelleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stelle
        fields = "__all__"


class TextSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Text
        fields = "__all__"


