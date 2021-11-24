from rest_framework import serializers
from topics.models import TextTopicRelation, Topic, ModelingProcess


class TextTopicRelationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TextTopicRelation
        fields = "__all__"
        depth = 1


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"
        depth = 1


class ModelingProcessSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ModelingProcess
        fields = "__all__"
        depth = 1
