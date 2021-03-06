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
                    'pi_norm_id',
                    'description',
                    'has_stelle__text',
                    'has_stelle__text__autor',
                    'has_stelle__key_word',
                    css_id="more"
                )
            )
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
            'exactish_geom': LeafletWidget(),
            'fuzzy_geom': LeafletWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(SpatialCoverageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


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
                'key_word',
                'stelle',
                'stelle__text__autor',
                'stelle__text__not_before',
                'stelle__text__not_after',
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
                'name',
                'gnd_id',
                'ort',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_pk',
                    'name_lat',
                    'name_en',
                    'name_fr',
                    'name_it',
                    'jahrhundert',
                    'start_date',
                    'end_date',
                    'kommentar',
                    'rvn_text_autor_autor__rvn_stelle_text_text__key_word',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
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
                'rvn_stelle_key_word_keyword__text__not_before',
                'rvn_stelle_key_word_keyword__text__not_after',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_pk',
                    'stichwort',
                    'rvn_stelle_key_word_keyword__text__autor',
                    'art',
                    'wurzel',
                    'kommentar',
                    'varianten',
                    'rvn_stelle_key_word_keyword',
                    'rvn_stelle_key_word_keyword__text',
                    'rvn_stelle_key_word_keyword__text__autor__ort',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
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
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_pk',
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
                    'legacy_id',
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
        fields = "__all__"

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
                'id',
                'zitat',
                'text',
                'text__autor',
                'key_word',
                'use_case',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_pk',
                    'summary',
                    'translation',
                    'kommentar',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
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
                'id',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'legacy_pk',
                    'autor',
                    'title',
                    'jahrhundert',
                    'not_before',
                    'not_after',
                    'edition',
                    'art',
                    'ort',
                    'kommentar',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
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
