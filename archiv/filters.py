# generated by appcreator
import django_filters

from dal import autocomplete

from vocabs.models import SkosConcept
from . models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase,
)


class UseCaseListFilter(django_filters.FilterSet):

    class Meta:
        model = UseCase
        fields = '__all__'


class SpatialCoverageListFilter(django_filters.FilterSet):
    key_word = django_filters.ModelMultipleChoiceFilter(
        queryset=KeyWord.objects.all(),
        help_text=SpatialCoverage._meta.get_field('key_word').help_text,
        label=SpatialCoverage._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
    )
    stelle = django_filters.ModelMultipleChoiceFilter(
        queryset=Stelle.objects.all(),
        help_text=SpatialCoverage._meta.get_field('stelle').help_text,
        label=SpatialCoverage._meta.get_field('stelle').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:stelle-autocomplete",
        )
    )

    class Meta:
        model = SpatialCoverage
        fields = [
            'id',
            'key_word',
            'stelle',
        ]


class AutorListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('legacy_id').help_text,
        label=Autor._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('name').help_text,
        label=Autor._meta.get_field('name').verbose_name
    )
    gnd_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('gnd_id').help_text,
        label=Autor._meta.get_field('gnd_id').verbose_name
    )
    name_lat = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('name_lat').help_text,
        label=Autor._meta.get_field('name_lat').verbose_name
    )
    name_en = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('name_en').help_text,
        label=Autor._meta.get_field('name_en').verbose_name
    )
    name_fr = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('name_fr').help_text,
        label=Autor._meta.get_field('name_fr').verbose_name
    )
    name_it = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('name_it').help_text,
        label=Autor._meta.get_field('name_it').verbose_name
    )
    jahrhundert = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('jahrhundert').help_text,
        label=Autor._meta.get_field('jahrhundert').verbose_name
    )
    start_date = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('start_date').help_text,
        label=Autor._meta.get_field('start_date').verbose_name
    )
    end_date = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('end_date').help_text,
        label=Autor._meta.get_field('end_date').verbose_name
    )
    ort = django_filters.ModelMultipleChoiceFilter(
        queryset=Ort.objects.all(),
        help_text=Autor._meta.get_field('ort').help_text,
        label=Autor._meta.get_field('ort').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    kommentar = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('kommentar').help_text,
        label=Autor._meta.get_field('kommentar').verbose_name
    )

    class Meta:
        model = Autor
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'name',
            'gnd_id',
            'name_lat',
            'name_en',
            'name_fr',
            'name_it',
            'jahrhundert',
            'start_date',
            'end_date',
            'ort',
            'kommentar',
            ]


class KeyWordListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('legacy_id').help_text,
        label=KeyWord._meta.get_field('legacy_id').verbose_name
    )
    stichwort = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('stichwort').help_text,
        label=KeyWord._meta.get_field('stichwort').verbose_name
    )
    wurzel = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('wurzel').help_text,
        label=KeyWord._meta.get_field('wurzel').verbose_name
    )
    kommentar = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('kommentar').help_text,
        label=KeyWord._meta.get_field('kommentar').verbose_name
    )
    varianten = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('varianten').help_text,
        label=KeyWord._meta.get_field('varianten').verbose_name
    )

    class Meta:
        model = KeyWord
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'stichwort',
            'art',
            'wurzel',
            'kommentar',
            'varianten'
            ]


class OrtListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('legacy_id').help_text,
        label=Ort._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('name').help_text,
        label=Ort._meta.get_field('name').verbose_name
    )
    norm_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('norm_id').help_text,
        label=Ort._meta.get_field('norm_id').verbose_name
    )
    name_antik = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('name_antik').help_text,
        label=Ort._meta.get_field('name_antik').verbose_name
    )
    name_de = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('name_de').help_text,
        label=Ort._meta.get_field('name_de').verbose_name
    )
    name_fr = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('name_fr').help_text,
        label=Ort._meta.get_field('name_fr').verbose_name
    )
    name_it = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('name_it').help_text,
        label=Ort._meta.get_field('name_it').verbose_name
    )
    art = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="art"
        ),
        help_text=Ort._meta.get_field('art').help_text,
        label=Ort._meta.get_field('art').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/art",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )
    kategorie = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="kategorie"
        ),
        help_text=Ort._meta.get_field('kategorie').help_text,
        label=Ort._meta.get_field('kategorie').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/kategorie",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )
    kommentar = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('kommentar').help_text,
        label=Ort._meta.get_field('kommentar').verbose_name
    )

    class Meta:
        model = Ort
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'name',
            'norm_id',
            'name_antik',
            'name_de',
            'name_fr',
            'name_it',
            'long',
            'lat',
            'art',
            'kategorie',
            'kommentar',
            ]


class StelleListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('legacy_id').help_text,
        label=Stelle._meta.get_field('legacy_id').verbose_name
    )
    text = django_filters.ModelMultipleChoiceFilter(
        queryset=Text.objects.all(),
        help_text=Stelle._meta.get_field('text').help_text,
        label=Stelle._meta.get_field('text').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:text-autocomplete",
        )
    )
    summary = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('summary').help_text,
        label=Stelle._meta.get_field('summary').verbose_name
    )
    zitat = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('zitat').help_text,
        label=Stelle._meta.get_field('zitat').verbose_name
    )
    translation = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('translation').help_text,
        label=Stelle._meta.get_field('translation').verbose_name
    )
    key_word = django_filters.ModelMultipleChoiceFilter(
        queryset=KeyWord.objects.all(),
        help_text=Stelle._meta.get_field('key_word').help_text,
        label=Stelle._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
    )
    kommentar = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('kommentar').help_text,
        label=Stelle._meta.get_field('kommentar').verbose_name
    )

    class Meta:
        model = Stelle
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'text',
            'summary',
            'zitat',
            'translation',
            'key_word',
            'kommentar',
            'use_case'
            ]


class TextListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('legacy_id').help_text,
        label=Text._meta.get_field('legacy_id').verbose_name
    )
    autor = django_filters.ModelMultipleChoiceFilter(
        queryset=Autor.objects.all(),
        help_text=Text._meta.get_field('autor').help_text,
        label=Text._meta.get_field('autor').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        )
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('title').help_text,
        label=Text._meta.get_field('title').verbose_name
    )
    jahrhundert = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('jahrhundert').help_text,
        label=Text._meta.get_field('jahrhundert').verbose_name
    )
    start_date = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('start_date').help_text,
        label=Text._meta.get_field('start_date').verbose_name
    )
    end_date = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('end_date').help_text,
        label=Text._meta.get_field('end_date').verbose_name
    )
    art = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="art"
        ),
        help_text=Text._meta.get_field('art').help_text,
        label=Text._meta.get_field('art').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/art",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )
    ort = django_filters.ModelMultipleChoiceFilter(
        queryset=Ort.objects.all(),
        help_text=Text._meta.get_field('ort').help_text,
        label=Text._meta.get_field('ort').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    kommentar = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('kommentar').help_text,
        label=Text._meta.get_field('kommentar').verbose_name
    )

    class Meta:
        model = Text
        fields = [
            'id',
            'legacy_id',
            'legacy_pk',
            'autor',
            'title',
            'jahrhundert',
            'start_date',
            'end_date',
            'edition',
            'art',
            'ort',
            'kommentar',
            ]


