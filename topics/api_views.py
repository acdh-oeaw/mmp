# import django_filters.rest_framework
import django_filters.rest_framework
from rest_framework import viewsets

from topics.filters import TextTopicRelationListFilter

from topics.models import (
    Topic,
    TextTopicRelation,
    ModelingProcess
)
from topics.api_serializers import (
    TopicSerializer,
    TextTopicRelationSerializer,
    ModelingProcessSerializer
)


class ModelingProcessViewSet(viewsets.ModelViewSet):
    queryset = ModelingProcess.objects.all()
    serializer_class = ModelingProcessSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TextTopicRelationViewSet(viewsets.ModelViewSet):
    queryset = TextTopicRelation.objects.all()
    serializer_class = TextTopicRelationSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TextTopicRelationListFilter
