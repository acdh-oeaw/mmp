# generated by appcreator
# import django_filters
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
    Event
)


def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(id__in=values)


DATE_LOOKUP_CHOICES = [
    ('exact', 'Equals'),
    ('gt', 'Greater than'),
    ('lt', 'Less than')
]

CHAR_LOOKUP_CHOICES = [
    ('icontains', 'Contains'),
    ('iexact', 'Equals'),
    ('istartswith', 'Starts with'),
    ('iendswith', 'Ends with')
]


class UseCaseListFilter(django_filters.FilterSet):
    ids = django_filters.CharFilter(method=filter_by_ids)
    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=UseCase._meta.get_field('title').help_text,
        label=UseCase._meta.get_field('title').verbose_name,
    )
    principal_investigator = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=UseCase._meta.get_field('principal_investigator').help_text,
        label=UseCase._meta.get_field('principal_investigator').verbose_name
    )
    pi_norm_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=UseCase._meta.get_field('pi_norm_id').help_text,
        label=UseCase._meta.get_field('pi_norm_id').verbose_name
    )
    description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=UseCase._meta.get_field('description').help_text,
        label=UseCase._meta.get_field('description').verbose_name
    )
    has_stelle__text = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Text.objects.all(),
        help_text="Related Text",
        label="Text",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:text-autocomplete",
        )
    )
    has_stelle__text__autor = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Autor.objects.all(),
        help_text="Related Authors",
        label="Author",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        )
    )
    has_stelle__key_word = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=KeyWord.objects.all(),
        help_text="Related Keywords",
        label="Keywords",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
    )

    class Meta:
        model = UseCase
        fields = ['id', ]


class SpatialCoverageListFilter(django_filters.FilterSet):
    key_word = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=KeyWord.objects.all(),
        help_text=SpatialCoverage._meta.get_field('key_word').help_text,
        label=SpatialCoverage._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
    )
    stelle = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Stelle.objects.all(),
        help_text=SpatialCoverage._meta.get_field('stelle').help_text,
        label=SpatialCoverage._meta.get_field('stelle').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:stelle-autocomplete",
        )
    )
    stelle__start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not before",
        label="Stelle not before"
    )
    stelle__end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not after",
        label="Stelle not after"
    )
    stelle__text__not_before = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not before",
        label="Text not before"
    )
    stelle__text__not_after = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not after",
        label="Text not after"
    )
    stelle__text__autor = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Autor.objects.all(),
        help_text="Related Authors",
        label="Author",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
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
    ids = django_filters.CharFilter(method=filter_by_ids)
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Autor._meta.get_field('legacy_id').help_text,
        label=Autor._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('name').help_text,
        label=Autor._meta.get_field('name').verbose_name
    )
    gnd_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('gnd_id').help_text,
        label=Autor._meta.get_field('gnd_id').verbose_name
    )
    name_lat = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('name_lat').help_text,
        label=Autor._meta.get_field('name_lat').verbose_name
    )
    name_en = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('name_en').help_text,
        label=Autor._meta.get_field('name_en').verbose_name
    )
    name_fr = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('name_fr').help_text,
        label=Autor._meta.get_field('name_fr').verbose_name
    )
    name_it = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('name_it').help_text,
        label=Autor._meta.get_field('name_it').verbose_name
    )
    jahrhundert = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('jahrhundert').help_text,
        label=Autor._meta.get_field('jahrhundert').verbose_name
    )
    start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('start_date').help_text,
        label=Autor._meta.get_field('start_date').verbose_name
    )
    end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('end_date').help_text,
        label=Autor._meta.get_field('end_date').verbose_name
    )
    ort = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Ort.objects.all(),
        help_text=Autor._meta.get_field('ort').help_text,
        label=Autor._meta.get_field('ort').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    kommentar = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Autor._meta.get_field('kommentar').help_text,
        label=Autor._meta.get_field('kommentar').verbose_name
    )
    rvn_text_autor_autor__rvn_stelle_text_text__key_word = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=KeyWord.objects.all(),
        label="Keywords",
        help_text="Keywords für Texte von diesen Autoren",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
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
    ids = django_filters.CharFilter(method=filter_by_ids)
    rvn_stelle_key_word_keyword__text__autor = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Autor.objects.all(),
        label="Autor",
        help_text="Stichworte wurde von diesen Autoren verwendet",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        )
    )
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=KeyWord._meta.get_field('legacy_id').help_text,
        label=KeyWord._meta.get_field('legacy_id').verbose_name
    )
    stichwort = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=KeyWord._meta.get_field('stichwort').help_text,
        label=KeyWord._meta.get_field('stichwort').verbose_name
    )
    wurzel = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=KeyWord._meta.get_field('wurzel').help_text,
        label=KeyWord._meta.get_field('wurzel').verbose_name
    )
    kommentar = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=KeyWord._meta.get_field('kommentar').help_text,
        label=KeyWord._meta.get_field('kommentar').verbose_name
    )
    varianten = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=KeyWord._meta.get_field('varianten').help_text,
        label=KeyWord._meta.get_field('varianten').verbose_name
    )
    rvn_stelle_key_word_keyword = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Stelle.objects.all(),
        label="Stelle",
        help_text="Stichworte stehen mit diesen Stellen in Verbindung",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:stelle-autocomplete",
        )
    )
    rvn_stelle_key_word_keyword__text = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Text.objects.all(),
        label="Text",
        help_text="Stichworte stehen mit diesen Texten in Verbindung",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:text-autocomplete",
        )
    )
    rvn_stelle_key_word_keyword__text__autor__ort = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Ort.objects.all(),
        label="Ort",
        help_text="Stichworte stehen mit diesen Orten in Verbindung",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    rvn_stelle_key_word_keyword__text__not_before = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not before",
        label="Text not before"
    )
    rvn_stelle_key_word_keyword__text__not_after = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not after",
        label="Text not after"
    )
    rvn_stelle_key_word_keyword__start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not before",
        label="Stelle not before"
    )
    rvn_stelle_key_word_keyword__end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not after",
        label="Stelle not after"
    )

    class Meta:
        model = KeyWord
        fields = [
            'rvn_stelle_key_word_keyword__text__autor',
            'id',
            'legacy_id',
            'legacy_pk',
            'stichwort',
            'art',
            'wurzel',
            'kommentar',
            'varianten',
            'rvn_stelle_key_word_keyword__text__not_before',
            'rvn_stelle_key_word_keyword__text__not_after'
        ]


class OrtListFilter(django_filters.FilterSet):
    ids = django_filters.CharFilter(method=filter_by_ids)
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Ort._meta.get_field('legacy_id').help_text,
        label=Ort._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('name').help_text,
        label=Ort._meta.get_field('name').verbose_name
    )
    norm_id = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('norm_id').help_text,
        label=Ort._meta.get_field('norm_id').verbose_name
    )
    name_antik = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('name_antik').help_text,
        label=Ort._meta.get_field('name_antik').verbose_name
    )
    name_de = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('name_de').help_text,
        label=Ort._meta.get_field('name_de').verbose_name
    )
    name_fr = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('name_fr').help_text,
        label=Ort._meta.get_field('name_fr').verbose_name
    )
    name_it = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Ort._meta.get_field('name_it').help_text,
        label=Ort._meta.get_field('name_it').verbose_name
    )
    art = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=SkosConcept.objects.filter(
            collection__name="place_art"
        ),
        help_text=Ort._meta.get_field('art').help_text,
        label=Ort._meta.get_field('art').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/place_art"
        )
    )
    kategorie = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=SkosConcept.objects.filter(
            collection__name="kategorie"
        ),
        help_text=Ort._meta.get_field('kategorie').help_text,
        label=Ort._meta.get_field('kategorie').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/kategorie"
        )
    )
    kommentar = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
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
    ids = django_filters.CharFilter(method=filter_by_ids)
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Stelle._meta.get_field('legacy_id').help_text,
        label=Stelle._meta.get_field('legacy_id').verbose_name
    )
    text = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Text.objects.all(),
        help_text=Stelle._meta.get_field('text').help_text,
        label=Stelle._meta.get_field('text').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:text-autocomplete",
        )
    )
    text__autor = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Autor.objects.all(),
        help_text="Related Authors",
        label="Author",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        )
    )
    ort = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Ort.objects.all(),
        help_text="Related Places",
        label="Places",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    summary = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Stelle._meta.get_field('summary').help_text,
        label=Stelle._meta.get_field('summary').verbose_name
    )
    zitat = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Stelle._meta.get_field('zitat').help_text,
        label=Stelle._meta.get_field('zitat').verbose_name
    )
    translation = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Stelle._meta.get_field('translation').help_text,
        label=Stelle._meta.get_field('translation').verbose_name
    )
    key_word = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=KeyWord.objects.all(),
        help_text=Stelle._meta.get_field('key_word').help_text,
        label=Stelle._meta.get_field('key_word').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:keyword-autocomplete",
        )
    )
    use_case = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=UseCase.objects.all(),
        help_text="Related UseCase",
        label="UseCase",
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:usecase-autocomplete",
        )
    )
    kommentar = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Stelle._meta.get_field('kommentar').help_text,
        label=Stelle._meta.get_field('kommentar').verbose_name
    )
    start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not before",
        label="Stelle not before"
    )
    end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Stelle not after",
        label="Stelle not after"
    )
    text__start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not before",
        label="Text not before"
    )
    text__end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text="Text not after",
        label="Text not after"
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
    ids = django_filters.CharFilter(method=filter_by_ids)
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Text._meta.get_field('legacy_id').help_text,
        label=Text._meta.get_field('legacy_id').verbose_name
    )
    autor = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Autor.objects.all(),
        help_text=Text._meta.get_field('autor').help_text,
        label=Text._meta.get_field('autor').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:autor-autocomplete",
        )
    )
    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('title').help_text,
        label=Text._meta.get_field('title').verbose_name
    )
    jahrhundert = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('jahrhundert').help_text,
        label=Text._meta.get_field('jahrhundert').verbose_name
    )
    not_before = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('not_before').help_text,
        label=Text._meta.get_field('not_before').verbose_name
    )
    not_after = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('not_after').help_text,
        label=Text._meta.get_field('not_after').verbose_name
    )
    edition = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('edition').help_text,
        label=Text._meta.get_field('edition').verbose_name
    )
    art = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=SkosConcept.objects.filter(
            collection__name="art"
        ),
        help_text=Text._meta.get_field('art').help_text,
        label=Text._meta.get_field('art').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/art",
        )
    )
    ort = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Ort.objects.all(),
        help_text=Text._meta.get_field('ort').help_text,
        label=Text._meta.get_field('ort').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )
    kommentar = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Text._meta.get_field('kommentar').help_text,
        label=Text._meta.get_field('kommentar').verbose_name
    )
    rvn_stelle_text_text__key_word = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=KeyWord.objects.all(),
        help_text='Keyword',
        label='Keyword',
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:ort-autocomplete",
        )
    )

    class Meta:
        model = Text
        fields = [
            'id',
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


class EventListFilter(django_filters.FilterSet):
    title = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('title').help_text,
        label=Event._meta.get_field('title').verbose_name
    )
    description = django_filters.LookupChoiceFilter(
        lookup_choices=CHAR_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('description').help_text,
        label=Event._meta.get_field('description').verbose_name
    )
    start_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('start_date').help_text,
        label=Event._meta.get_field('start_date').verbose_name
    )
    end_date = django_filters.LookupChoiceFilter(
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Event._meta.get_field('end_date').help_text,
        label=Event._meta.get_field('end_date').verbose_name
    )

    class Meta:
        model = Event
        fields = [
            'title',
        ]
