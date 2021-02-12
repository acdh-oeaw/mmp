# API serializers for archiv created by appcreator
from rest_framework import serializers
from archiv.models import (
    Autor,
    Edition,
    KeyWord,
    Ort,
    Stelle,
    Text
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


