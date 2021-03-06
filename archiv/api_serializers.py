# API serializers for archiv created by appcreator
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from archiv.models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase,
)


class UseCaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UseCase
        fields = "__all__"
        depth = 1


class SpatialCoverageSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):

    class Meta:
        model = SpatialCoverage
        geo_field = 'fuzzy_geom'
        auto_bbox = True
        fields = (
            'stelle',
            'key_word',
            'fuzzyness'
        )
        depth = 3


class ConeSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):
    cone = GeometrySerializerMethodField()

    def get_cone(self, res):
        return res.convex_hull

    class Meta:
        model = SpatialCoverage
        geo_field = 'cone'
        auto_bbox = False
        fields = (
            'stelle',
            'key_word',
            'fuzzyness'
        )
        depth = 3


class AutorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Autor
        fields = "__all__"
        depth = 1


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
        depth = 1


class TextSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Text
        fields = "__all__"
        depth = 1
