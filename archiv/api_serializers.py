# API serializers for archiv created by appcreator
from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometrySerializerMethodField,
)
from markdownify import markdownify as md
from archiv.models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase,
    Event,
)
from story_map.models import Story, Slide


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 0


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"
        depth = 2


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = "__all__"
        depth = 1


class UseCaseSerializer(serializers.ModelSerializer):
    as_md = serializers.SerializerMethodField()

    class Meta:
        model = UseCase
        fields = "__all__"
        depth = 1

    def get_as_md(self, obj):
        md_string = ""
        if isinstance(obj.story_map, str):
            md_string = md(obj.story_map)
        else:
            md_string = ""
        return f"{md_string}"


class SpatialCoverageSerializer(GeoFeatureModelSerializer, serializers.ModelSerializer):
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()

    class Meta:
        model = SpatialCoverage
        geo_field = "fuzzy_geom"
        auto_bbox = True
        fields = (
            "id",
            "key_word",
            "fuzzyness",
            "stelle",
            "texts",
            "kommentar",
        )
        depth = 1


class SpatialCoverageGroupSerializer(
    GeoFeatureModelSerializer, serializers.ModelSerializer
):
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()

    class Meta:
        model = SpatialCoverage
        geo_field = "geom_collection"
        auto_bbox = True
        fields = (
            "id",
            "key_word",
            "fuzzyness",
            "stelle",
            "texts",
        )
        depth = 1


class ConeSerializer(GeoFeatureModelSerializer, serializers.ModelSerializer):
    cone = GeometrySerializerMethodField()
    stelle = serializers.ReadOnlyField(source="stellen")
    texts = serializers.ReadOnlyField()

    def get_cone(self, res):
        return res.convex_hull

    class Meta:
        model = SpatialCoverage
        geo_field = "cone"
        auto_bbox = False
        fields = (
            "id",
            "key_word",
            "fuzzyness",
            "stelle",
            "texts",
        )
        depth = 1


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]
        depth = 1


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]


class OrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ort
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]


class GeoJsonOrtSerializer(GeoFeatureModelSerializer, serializers.ModelSerializer):

    art = serializers.ReadOnlyField(source="kind")

    class Meta:
        model = Ort
        geo_field = "coords"
        fields = [
            "id",
            "name",
            "name_antik",
            "name_de",
            "name_fr",
            "name_gr",
            "art",
            "kategorie",
        ]
        depth = 0


class FuzzyGeoJsonOrtSerializer(GeoFeatureModelSerializer, serializers.ModelSerializer):

    art = serializers.ReadOnlyField(source="kind")

    class Meta:
        model = Ort
        geo_field = "fuzzy_geom"
        fields = [
            "id",
            "name",
            "name_antik",
            "name_de",
            "name_fr",
            "name_gr",
            "art",
            "kategorie",
        ]
        depth = 0


class StelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stelle
        exclude = [
            "legacy_id",
            "legacy_pk",
            "orig_data_csv",
            "lemmata",
            "use_case"
        ]
        depth = 2


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        exclude = ["legacy_id", "legacy_pk", "orig_data_csv"]
        depth = 1
