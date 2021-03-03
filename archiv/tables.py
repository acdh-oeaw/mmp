# generated by appcreator
import django_tables2 as tables

from browsing.browsing_utils import MergeColumn
from . models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase
)


class UseCaseTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = UseCase
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class SpatialCoverageTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = SpatialCoverage
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class AutorTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Autor
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class KeyWordTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = KeyWord
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class OrtTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = Ort
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class StelleTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')
    key_word = tables.columns.ManyToManyColumn()
    use_case = tables.columns.ManyToManyColumn()

    class Meta:
        model = Stelle
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class TextTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')
    autor = tables.columns.ManyToManyColumn()
    ort = tables.columns.ManyToManyColumn()

    class Meta:
        model = Text
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}
