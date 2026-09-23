# import django_filters.rest_framework
import django_filters.rest_framework
from rest_framework import viewsets

from topics.api_serializers import (
    ModelingProcessSerializer,
    StopWordSerializer,
    TextTopicRelationSerializer,
    TopicSerializer,
)
from topics.filters import TextTopicRelationListFilter
from topics.models import ModelingProcess, StopWord, TextTopicRelation, Topic


class StopWordViewSet(viewsets.ModelViewSet):
    queryset = StopWord.objects.all().distinct()
    serializer_class = StopWordSerializer


class ModelingProcessViewSet(viewsets.ModelViewSet):
    queryset = ModelingProcess.objects.all().distinct()
    serializer_class = ModelingProcessSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().distinct()
    serializer_class = TopicSerializer


class TextTopicRelationViewSet(viewsets.ModelViewSet):
    queryset = TextTopicRelation.objects.all().distinct()
    serializer_class = TextTopicRelationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TextTopicRelationListFilter
