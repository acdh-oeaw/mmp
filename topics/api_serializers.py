from rest_framework import serializers
from topics.models import TextTopicRelation, Topic, ModelingProcess, StopWord


class TextTopicRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextTopicRelation
        fields = "__all__"
        depth = 0


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"
        depth = 1


class ModelingProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelingProcess
        fields = "__all__"
        depth = 1


class StopWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = StopWord
        fields = "__all__"
        depth = 0
