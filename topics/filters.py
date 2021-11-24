import django_filters
from django_filters.rest_framework import FilterSet
from django.forms import FloatField

from archiv.models import Stelle
from . models import (
    Topic
)

NUMBER_LOOKUP_CHOICES = [
    ('exact', 'Equals'),
    ('gt', 'Greater than'),
    ('lt', 'Less than')
]


def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(id__in=values)


class TextTopicRelationListFilter(FilterSet):
    ids = django_filters.CharFilter(method=filter_by_ids)
    text = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Stelle.objects.all(),
        help_text="related passages",
        label="Passages",
    )
    topic = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Topic.objects.all(),
        help_text="related topics",
        label="Topics",
    )
    weight = django_filters.LookupChoiceFilter(
        field_class=FloatField,
        lookup_choices=NUMBER_LOOKUP_CHOICES
    )
