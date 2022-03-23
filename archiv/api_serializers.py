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
from story_map.models import Story, Slide


class StorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Story
        fields = "__all__"
        depth = 2


class SlideSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Slide
        fields = "__all__"
        depth = 1


class UseCaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UseCase
        fields = "__all__"
        depth = 1


class SpatialCoverageSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()
    places = serializers.ReadOnlyField()

    class Meta:
        model = SpatialCoverage
        geo_field = 'fuzzy_geom'
        auto_bbox = True
        fields = (
            'id',
            'key_word',
            'fuzzyness',
            'stelle',
            'texts',
            'places'
        )
        depth = 1


class SpatialCoverageGroupSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()
    places = serializers.ReadOnlyField()

    class Meta:
        model = SpatialCoverage
        geo_field = 'geom_collection'
        auto_bbox = True
        fields = (
            'id',
            'key_word',
            'fuzzyness',
            'stelle',
            'texts',
            'places'
        )
        depth = 1


class ConeSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):
    cone = GeometrySerializerMethodField()
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()
    places = serializers.ReadOnlyField()

    def get_cone(self, res):
        return res.convex_hull

    class Meta:
        model = SpatialCoverage
        geo_field = 'cone'
        auto_bbox = False
        fields = (
            'id',
            'key_word',
            'fuzzyness',
            'stelle',
            'texts',
            'places'
        )
        depth = 1


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


class GeoJsonOrtSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):

    class Meta:
        model = Ort
        geo_field = 'coords'
        fields = [
            'id', 'name', 'name_antik', 'name_de',
            'name_fr', 'name_gr', 'art', 'kategorie'
        ]
        depth = 0


class FuzzyGeoJsonOrtSerializer(
    GeoFeatureModelSerializer, serializers.HyperlinkedModelSerializer
):

    class Meta:
        model = Ort
        geo_field = 'fuzzy_geom'
        fields = [
            'id', 'name', 'name_antik', 'name_de',
            'name_fr', 'name_gr', 'art', 'kategorie'
        ]
        depth = 0


class StelleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stelle
        exclude = [
            'lemmata',
        ]
        depth = 2


class TextSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Text
        fields = "__all__"
        depth = 1
