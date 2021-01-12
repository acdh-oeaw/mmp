# generated by appcreator
import django_tables2 as tables
from django_tables2.utils import A

from browsing.browsing_utils import MergeColumn
from . models import (
    Autor,
    Ort
)


class AutorTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Autor
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class OrtTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Ort
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}

