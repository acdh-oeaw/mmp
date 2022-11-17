from rest_framework import serializers

from . models import GeoJsonLayer


class GeoJsonLayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoJsonLayer
        fields = "__all__"
        depth = 0
