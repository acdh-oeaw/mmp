# generated by appcreator
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit,  Layout, Fieldset
)
from crispy_forms.bootstrap import Accordion, AccordionGroup
from dal import autocomplete
from leaflet.forms.widgets import LeafletWidget

from vocabs.models import SkosConcept
from . models import (
    Autor,
    Edition,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage
)


class SpatialCoverageForm(forms.ModelForm):

    class Meta:
        model = SpatialCoverage
        fields = "__all__"
        widgets = {
            'stelle': autocomplete.ModelSelect2(
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

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class EditionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EditionFilterFormHelper, self).__init__(*args, **kwargs)
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
                    
                    'zitat',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class EditionForm(forms.ModelForm):

    class Meta:
        model = Edition
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EditionForm, self).__init__(*args, **kwargs)
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
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'stichwort',
                    'art',
                    'wurzel',
                    'kommentar',
                    'varianten',
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
        queryset=SkosConcept.objects.filter(collection__name="art")
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
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'legacy_pk',
                    'text',
                    'summary',
                    'zitat',
                    'translation',
                    'key_word',
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
                    'start_date',
                    'end_date',
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

    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


