# generated by appcreator
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit,
    Layout,
    Fieldset
)
from crispy_forms.bootstrap import Accordion, AccordionGroup
from dal import autocomplete
from leaflet.forms.widgets import LeafletWidget

from vocabs.models import SkosConcept

from . widgets import GeoColWidget
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


class SpatialCoverageForm(forms.ModelForm):

    class Meta:
        model = SpatialCoverage
        fields = "__all__"
        widgets = {
            'stelle': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:stelle-autocomplete'
            ),
            'key_word': autocomplete.ModelSelect2(
                url='archiv-ac:keyword-autocomplete'
            ),
            'fuzzy_geom': LeafletWidget(),
            'geom_collection': GeoColWidget()
        }

    def __init__(self, *args, **kwargs):
        super(SpatialCoverageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class UseCaseForm(forms.ModelForm):

    class Meta:
        model = UseCase
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UseCaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class UseCaseFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(UseCaseFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'title',
                'principal_investigator',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'id',
                    'pi_norm_id',
                    'description',
                    'has_stelle__text',
                    'has_stelle__text__art',
                    'has_stelle__text__autor',
                    'has_stelle__key_word',
                    css_id="more"
                )
            )
        )


class SpatialCoverageFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SpatialCoverageFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'show_labels',
                'key_word',
                'stelle__use_case',
                'stelle__ort',
                'stelle__text__ort',
                'stelle',
                'stelle__start_date',
                'stelle__end_date',
                'stelle__text__autor',
                'stelle__text__art',
                'stelle__text__not_before',
                'stelle__text__not_after',
                'stelle__text__autor__start_date_year',
                'stelle__text__autor__end_date_year',
                css_id="basic_search_fields"
            ),
        )


class AutorFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AutorFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'has_usecase',
                'name',
                'gnd_id',
                'ort',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'name_lat',
                    'name_en',
                    'name_fr',
                    'name_it',
                    'jahrhundert',
                    'start_date_year',
                    'end_date_year',
                    'kommentar',
                    'rvn_text_autor_autor',
                    'rvn_text_autor_autor__art',
                    'rvn_text_autor_autor__rvn_stelle_text_text__key_word',
                    'rvn_text_autor_autor__rvn_stelle_text_text__key_word__art',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    css_id="admin_search"
                ),
            )
        )


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = "__all__"
        widgets = {
            'ort': autocomplete.ModelSelect2(
                url='archiv-ac:ort-autocomplete'
            )
        }

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class KeyWordFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(KeyWordFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'stichwort',
                'has_usecase',
                'rvn_stelle_key_word_keyword__use_case',
                'rvn_stelle_key_word_keyword__start_date',
                'rvn_stelle_key_word_keyword__end_date',
                'rvn_stelle_key_word_keyword__text__not_before',
                'rvn_stelle_key_word_keyword__text__not_after',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'rvn_stelle_key_word_keyword__text__autor',
                    'art',
                    'wurzel',
                    'kommentar',
                    'varianten',
                    'rvn_stelle_key_word_keyword',
                    'rvn_stelle_key_word_keyword__text',
                    'rvn_stelle_key_word_keyword__text__autor__ort',
                    'rvn_stelle_key_word_keyword__text__art',
                    'rvn_stelle_key_word_keyword__text__autor__start_date_year',
                    'rvn_stelle_key_word_keyword__text__autor__end_date_year',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    css_id="admin_search"
                ),
            )
        )


class KeyWordForm(forms.ModelForm):

    class Meta:
        model = KeyWord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(KeyWordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class OrtFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(OrtFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'name',
                'name_antik',
                'norm_id',
                'rvn_autor_ort_ort',
                'rvn_text_ort_ort',
                'rvn_text_ort_ort__rvn_stelle_text_text__key_word',
                'rvn_text_ort_ort__rvn_stelle_text_text__use_case',
                'rvn_text_ort_ort__rvn_stelle_text_text',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'name_de',
                    'name_fr',
                    'name_it',
                    'long',
                    'lat',
                    'art',
                    'kategorie',
                    'kommentar',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    css_id="admin_search"
                ),
            )
        )


class OrtForm(forms.ModelForm):
    art = forms.ModelChoiceField(
        required=False,
        label="Art des Ortes",
        queryset=SkosConcept.objects.filter(collection__name="place_art")
    )
    kategorie = forms.ModelChoiceField(
        required=False,
        label="Kategorie des Ortes",
        queryset=SkosConcept.objects.filter(collection__name="kategorie")
    )

    class Meta:
        model = Ort
        widgets = {
            'fuzzy_geom': GeoColWidget(),
        }
        exclude = ['coords', ]

    def __init__(self, *args, **kwargs):
        super(OrtForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class StelleFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(StelleFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'has_usecase',
                'id',
                'zitat',
                'text',
                'text__autor',
                'text__autor_and',
                'text__art',
                'text__ort',
                'text__ort_and',
                'key_word',
                'key_word_and',
                'use_case',
                'key_word__art',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Filter by Date',
                    'start_date',
                    'end_date',
                    'text__start_date',
                    'text__end_date',
                    'text__autor__start_date_year',
                    'text__autor__end_date_year',
                    css_id="time_filter"
                ),
                AccordionGroup(
                    'Advanced search',
                    'summary',
                    'translation',
                    'kommentar',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    css_id="admin_search"
                ),
            )
        )


class StelleForm(forms.ModelForm):

    class Meta:
        model = Stelle
        fields = "__all__"
        widgets = {
            'text': autocomplete.ModelSelect2(
                url='archiv-ac:text-autocomplete'
            ),
            'key_word': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:keyword-autocomplete'
            ),
            'ort': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:ort-autocomplete'
            )
        }

    def __init__(self, *args, **kwargs):
        super(StelleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TextFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TextFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'title',
                'autor',
                'has_usecase',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Content',
                    'rvn_stelle_text_text__key_word',
                    'rvn_stelle_text_text__key_word__art',
                    'edition',
                    'art',
                    css_id="entities"
                ),
                AccordionGroup(
                    'Dates',
                    'jahrhundert',
                    'not_before',
                    'not_after',
                    'start_date',
                    'end_date',
                    'autor__start_date_year',
                    'autor__end_date_year',
                    css_id="dates"
                ),
                AccordionGroup(
                    'admin',
                    'id',
                    'kommentar',
                    css_id="admin_search"
                ),
            )
        )


class TextForm(forms.ModelForm):
    art = forms.ModelChoiceField(
        required=False,
        label="Textart",
        queryset=SkosConcept.objects.filter(collection__name="art")
    )

    class Meta:
        model = Text
        fields = "__all__"
        widgets = {
            'autor': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:autor-autocomplete'
            ),
            'ort': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:ort-autocomplete'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class EventFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EventFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'title',
                'description',
                'use_case',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'start_date',
                    'end_date',
                    css_id="more"
                ),
            ),
        )


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
        self.fields['start_date'].required = True
