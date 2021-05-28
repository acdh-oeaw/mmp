# generated by appcreator
import logging

from django.db import models
from django.urls import reverse
from django.contrib.gis.db.models import PolygonField
from django.utils.functional import cached_property

from vocabs.models import SkosConcept

from browsing.browsing_utils import model_to_dict

logger = logging.getLogger(__name__)


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class UseCase(models.Model):
    """ Use Case in regards of a specific research questions """
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Title",
        help_text="Title of the Use Case",
    ).set_extra(
        is_public=True,
        arche_prop="hasTitle",
    )
    principal_investigator = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="PI",
        help_text="Principal Investigator of the Use Case",
    ).set_extra(
        is_public=True,
        arche_prop="hasPrincipalInvestigator",
    )
    pi_norm_id = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Some Norm-ID of the PI",
        help_text="e.g. GND-ID or ORCID",
    ).set_extra(
        is_public=True,
        arche_prop="hasPrincipalInvestigator",
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="Short Description of the Use Case",
    ).set_extra(
        is_public=True,
        arche_prop="hasDescription",
    )

    class Meta:

        ordering = [
            'title',
        ]
        verbose_name = "Use Case"

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @cached_property
    def get_texts(self):
        text = Text.objects.filter(
            rvn_stelle_text_text__use_case=self
        ).distinct()
        return text

    @cached_property
    def get_authors(self):
        author = Autor.objects.filter(
            rvn_text_autor_autor__in=self.get_texts
        ).distinct()
        return author

    @cached_property
    def get_keywords(self):
        keyword = KeyWord.objects.filter(
            rvn_stelle_key_word_keyword__use_case=self
        ).distinct()
        return keyword

    @cached_property
    def get_events(self):
        event = Event.objects.all()
        return event    

    @classmethod
    def get_source_table(self):
        return None

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:usecase_browse')

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:usecase_create')

    def get_absolute_url(self):
        return reverse('archiv:usecase_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:usecase_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:usecase_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:usecase_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:usecase_detail',
                kwargs={'pk': prev.first().id}
            )
        return False

    def get_timetable_data(self):
        time_table_data = []
        if self.get_texts:
            for x in self.get_texts:
                try:
                    time_table_data.append(
                        {
                            'id': x.id,
                            'start_date': int(x.start_date),
                            'end_date': x.end_date,
                            'ent_type': 'text',
                            'ent_title': x.title,
                            'ent_description': x.title,
                            'ent_detail_view': x.get_absolute_url()  
                        }
                    )
                except Exception:
                    pass
        if self.get_authors:
            for x in self.get_authors:
                try:
                    time_table_data.append(
                        {
                            'id': x.id,
                            'start_date': int(x.start_date),
                            'end_date': x.end_date,
                            'ent_type': 'autor',
                            'ent_title': x.name,
                            'ent_description': x.name,
                            'ent_detail_view': x.get_absolute_url()  
                        }
                    )
                except Exception:
                    pass                
        if self.get_events:        
            for x in self.get_events:
                try:
                    time_table_data.append(
                        {
                            'id': x.id,
                            'start_date': int(x.start_date),
                            'end_date': x.end_date,
                            'ent_type': 'event',
                            'ent_title': x.title,
                            'ent_description': x.description,
                            'ent_detail_view': x.get_absolute_url()  
                        }
                    ) 
                except Exception:
                    pass                   
        return sorted(time_table_data, key=lambda k: k['start_date'])


class SpatialCoverage(models.Model):
    """ Spatial Coverage of a Keyword bound to a specifc source document"""
    stelle = models.ManyToManyField(
        "Stelle",
        related_name='has_spatial_coverage',
        blank=True,
        verbose_name="Stelle",
        help_text="Stelle",
    ).set_extra(
        is_public=True,
    )
    key_word = models.ForeignKey(
        "KeyWord",
        related_name='has_spatial_coverage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Stichwort",
        help_text="Stichwort",
    ).set_extra(
        is_public=True,
        arche_prop="hasSubject",
    )

    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        arche_prop="hasNote",
    )
    fuzzy_geom = PolygonField(
        blank=True, null=True,
        verbose_name="unsichere Ortsangabe",
        help_text="Ungefähre Lokalisierung einer Region",
    ).set_extra(
        is_public=True,
        arche_prop="hasWkt",
    )
    fuzzyness = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)],
        blank=True,
        default=1,
        verbose_name="Sicherheitsindikator",
        help_text="1 sehr sicher, 10 sehr unsicher"
    ).set_extra(
        is_public=True,
    )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Spatial Coverage"

    def __str__(self):
        return f"{self.stelle.all()} - {self.key_word}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_source_table(self):
        return None

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:spatialcoverage_browse')

    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:spatialcoverage_create')

    def get_absolute_url(self):
        return reverse('archiv:spatialcoverage_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:spatialcoverage_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:spatialcoverage_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:spatialcoverage_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:spatialcoverage_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Autor(models.Model):
    """ Autor """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="aid",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="legacy ID: <value>",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (de)",
        help_text="Name (de)",
    ).set_extra(
        is_public=True,
        data_lookup="anamed",
        arche_prop="hasTitle",
    )
    gnd_id = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="GND ID",
        help_text="z.B. http://d-nb.info/gnd/118650130",
    ).set_extra(
        is_public=True,
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="GND-ID: <value>",
    )
    name_lat = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (lat)",
        help_text="Name (lat)",
    ).set_extra(
        is_public=True,
        data_lookup="anamelat",
        arche_prop="hasAlternativeTitle",
    )
    name_en = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (en)",
        help_text="Name (en)",
    ).set_extra(
        is_public=True,
        data_lookup="anameeng",
        arche_prop="hasAlternativeTitle",
    )
    name_fr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (fr)",
        help_text="Name (fr)",
    ).set_extra(
        is_public=True,
        data_lookup="anamefr",
        arche_prop="hasAlternativeTitle",
    )
    name_it = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (it)",
        help_text="Name (it)",
    ).set_extra(
        is_public=True,
        data_lookup="anameit",
        arche_prop="hasAlternativeTitle",
    )
    name_gr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (gr)",
        help_text="Name (gr)",
    ).set_extra(
        is_public=True,
        arche_prop="hasAlternativeTitle",
    )
    jahrhundert = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Jahrundert",
        help_text="Jahrhundert",
    ).set_extra(
        is_public=True,
        data_lookup="ajh",
    )
    start_date = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="von",
        help_text="von",
    ).set_extra(
        is_public=True,
        data_lookup="avon",
    )
    end_date = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="bis",
        help_text="bis",
    ).set_extra(
        is_public=True,
        data_lookup="abis",
    )
    ort = models.ForeignKey(
        "Ort",
        related_name='rvn_autor_ort_ort',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ort",
        help_text="Ort",
    ).set_extra(
        is_public=True,
        data_lookup="aort",
    )
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="akommentar",
        arche_prop="hasNote",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'legacy_pk',
        ]
        verbose_name = "Autor"

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:autor_browse')

    @classmethod
    def get_source_table(self):
        return "autor"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:autor_create')

    @cached_property
    def get_stellen(self):
        stellen = Stelle.objects.filter(
            text__autor=self
        ).distinct()
        return stellen

    @cached_property
    def get_keywords(self):
        keywords = KeyWord.objects.filter(
            rvn_stelle_key_word_keyword__in=self.get_stellen
        ).distinct()
        return keywords

    def get_absolute_url(self):
        return reverse('archiv:autor_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:autor_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:autor_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:autor_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:autor_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class KeyWord(models.Model):
    """ Keyword """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="stid",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="legacy ID: <value>",
    )
    stichwort = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Stichwort",
        help_text="Stichwort",
    ).set_extra(
        is_public=True,
        data_lookup="stichwort",
        arche_prop="hasTitle",
    )
    name_gr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (gr)",
        help_text="Name (gr)",
    ).set_extra(
        is_public=True,
        arche_prop="hasAlternativeTitle",
    )
    art = models.CharField(
        max_length=250,
        blank=True,
        choices=(
            ('Schlagwort', 'Schlagwort'),
            ('Eigenname', 'Eigenname'),
        ),
        verbose_name="Art des Stichworts",
        help_text="Art des Stichworts",
    ).set_extra(
        is_public=True,
        data_lookup="start",
    )
    varianten = models.TextField(
        blank=True,
        null=True,
        verbose_name="Varianten",
        help_text="Varianten, bitte mit ';' trennen"
    )
    wurzel = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Wurzel",
        help_text="Wurzel",
    ).set_extra(
        is_public=True,
        data_lookup="wurzel",
    )
    related_keyword = models.ManyToManyField(
        "KeyWord",
        related_name='rvn_related_keyword',
        blank=True,
        verbose_name="Stichwort",
        help_text="Steht in Verbindung zu anderem Stichwort",
    ).set_extra(
        is_public=True,
    )
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="anmerkung",
        arche_prop="hasNote",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'stichwort',
        ]
        verbose_name = "Keyword"

    def __str__(self):
        if self.stichwort:
            return f"{self.stichwort}, [wurzel: {self.wurzel}]"
        else:
            return "{}".format(self.legacy_id)

    @cached_property
    def get_texts(self):
        texts = Text.objects.filter(
            rvn_stelle_text_text__key_word=self
        ).distinct()
        return texts

    @cached_property
    def get_authors(self):
        authors = Autor.objects.filter(
            rvn_text_autor_autor__in=self.get_texts
        ).distinct()
        return authors

    @cached_property
    def get_orte(self):
        orte = Ort.objects.filter(
            rvn_autor_ort_ort__in=self.get_authors
        ).distinct()
        return orte

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:keyword_browse')

    @classmethod
    def get_source_table(self):
        return None

    @classmethod
    def get_natural_primary_key(self):
        return "stichwort"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:keyword_create')

    def get_absolute_url(self):
        return reverse('archiv:keyword_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:keyword_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:keyword_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:keyword_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:keyword_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Ort(models.Model):
    """ Ort """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="ortid",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="legacy ID: <value>",
    )
    name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (en)",
        help_text="Name (en)",
    ).set_extra(
        is_public=True,
        data_lookup="Ort_en",
        arche_prop="hasTitle",
    )
    norm_id = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Norm-ID",
        help_text="""z.B. 'https://gazetteer.dainst.org/place/2070134',\
            https://www.geonames.org/2772400 oder\
            https://pleiades.stoa.org/places/857050
        """,
    ).set_extra(
        is_public=True,
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="NormID: <value>",
    )
    name_antik = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (antik)",
        help_text="Name (antik)",
    ).set_extra(
        is_public=True,
        data_lookup="Ort_antik",
        arche_prop="hasAlternativeTitle",
    )
    name_de = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (de)",
        help_text="Name (de)",
    ).set_extra(
        is_public=True,
        data_lookup="Ort_de",
        arche_prop="hasAlternativeTitle",
    )
    name_fr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (fr)",
        help_text="Name (fr)",
    ).set_extra(
        is_public=True,
        data_lookup="Ort_fr",
        arche_prop="hasAlternativeTitle",
    )
    name_it = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (it)",
        help_text="Name (it)",
    ).set_extra(
        is_public=True,
        data_lookup="Ort_it",
        arche_prop="hasAlternativeTitle",
    )
    name_gr = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name (gr)",
        help_text="Name (gr)",
    ).set_extra(
        is_public=True,
        arche_prop="hasAlternativeTitle",
    )
    long = models.FloatField(
        blank=True, null=True,
        verbose_name="Längengrad",
        help_text="Längengrad",
    ).set_extra(
        is_public=True,
        data_lookup="KoordW",
    )
    lat = models.FloatField(
        blank=True, null=True,
        verbose_name="Breitengrad",
        help_text="Breitengrad",
    ).set_extra(
        is_public=True,
        data_lookup="KoordN",
    )
    art = models.ForeignKey(
        SkosConcept,
        related_name='rvn_ort_art_skosconcept',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Art des Ortes",
        help_text="Art des Ortes",
    ).set_extra(
        is_public=True,
        data_lookup="Art",
    )
    kategorie = models.ForeignKey(
        SkosConcept,
        related_name='rvn_ort_kategorie_skosconcept',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Kategorie des Ortes",
        help_text="Kategorie des Ortes",
    ).set_extra(
        is_public=True,
        data_lookup="Kategorie",
    )
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="Kommentar",
        arche_prop="hasNote",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'legacy_pk',
        ]
        verbose_name = "Ort"

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:ort_browse')

    @classmethod
    def get_source_table(self):
        return "orte"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:ort_create')

    def get_absolute_url(self):
        return reverse('archiv:ort_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:ort_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:ort_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:ort_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:ort_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Stelle(models.Model):
    """ Stelle """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="sid",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="legacy ID: <value>",
    )
    text = models.ForeignKey(
        "Text",
        related_name='rvn_stelle_text_text',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Text",
        help_text="Text",
    ).set_extra(
        is_public=True,
        data_lookup="stexttitel",
    )
    summary = models.TextField(
        blank=True, null=True,
        verbose_name="Zusammenfassung",
        help_text="Zusammenfassung",
    ).set_extra(
        is_public=True,
        data_lookup="ssummary",
        arche_prop="hasDescription",
    )
    zitat = models.TextField(
        blank=True, null=True,
        verbose_name="Zitat",
        help_text="Zitat",
    ).set_extra(
        is_public=True,
        data_lookup="szitat",
        arche_prop="hasDescription",
    )
    zitat_stelle = models.CharField(
        max_length=250,
        blank=True, null=True,
        verbose_name="Zitat Stelle",
        help_text="z.B. Seitenangaben",
    ).set_extra(
        is_public=True,
        arche_prop="hasNote",
    )
    translation = models.TextField(
        blank=True, null=True,
        verbose_name="Übersetzung",
        help_text="Übersetzung",
    ).set_extra(
        is_public=True,
        data_lookup="stranslation",
    )
    key_word = models.ManyToManyField(
        "KeyWord",
        related_name='rvn_stelle_key_word_keyword',
        blank=True,
        verbose_name="Stichwort",
        help_text="Stichwort",
    ).set_extra(
        is_public=True,
        arche_prop="hasSubject",
    )
    ort = models.ForeignKey(
        "Ort",
        related_name='rvn_stelle_ort_ort',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ort",
        help_text="Ort",
    ).set_extra(
        is_public=True,
        arche_prop="hasSpatialCoverage"
    )
    start_date = models.PositiveSmallIntegerField(
        blank=True, null=True,
        verbose_name="Start Date",
        help_text="e.g. '300'"
    ).set_extra(
        is_public=True,
        arche_prop="hasCoverageStartDate"
    )
    end_date = models.PositiveSmallIntegerField(
        blank=True, null=True,
        verbose_name="End Date",
        help_text="e.g. '1234'"
    ).set_extra(
        is_public=True,
        arche_prop="hasCoverageEndDate"
    )
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="skommentar",
        arche_prop="hasNote",
    )
    display_label = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="automatic created label"
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )
    use_case = models.ManyToManyField(
        "UseCase",
        related_name='has_stelle',
        blank=True,
        verbose_name="Use Case",
        help_text="Verwendet in Use Case",
    ).set_extra(
        is_public=True,
    )

    class Meta:

        ordering = [
            'legacy_pk',
        ]
        verbose_name = "Stelle"

    def save(self, *args, **kwargs):
        self.display_label = self.make_label()
        super(Stelle, self).save(*args, **kwargs)

    def make_label(self):
        try:
            label = f"{self.zitat[:35]}...; ({self.text}, {self.zitat_stelle})"
        except Exception as e:
            logger.error(
                f'Stelle.make_label in object: {self.id} threw error {e}'
            )
            label = "{}".format(self.id)
        return label[:249]

    def __str__(self):
        if self.display_label:
            return f"{self.display_label} [{self.id}]"
        else:
            return f"{self.id}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:stelle_browse')

    @classmethod
    def get_source_table(self):
        return "stelle"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:stelle_create')

    def get_absolute_url(self):
        return reverse('archiv:stelle_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:stelle_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:stelle_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:stelle_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:stelle_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Text(models.Model):
    """ Text """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    legacy_pk = models.IntegerField(
        blank=True, null=True,
        verbose_name="Primärschlüssel Alt",
        help_text="Primärschlüssel Alt",
    ).set_extra(
        is_public=False,
        data_lookup="tID",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="legacy ID: <value>",
    )
    autor = models.ManyToManyField(
        "Autor",
        related_name='rvn_text_autor_autor',
        blank=True,
        verbose_name="Autor",
        help_text="Autor",
    ).set_extra(
        is_public=True,
        data_lookup="tautor",
        arche_prop="hasAuthor",
    )
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Titel",
        help_text="Titel",
    ).set_extra(
        is_public=True,
        data_lookup="ttitel",
        arche_prop="hasTitle",
    )
    alt_title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Alternative(r) Titel",
        help_text="Alternative(r) Titel",
    ).set_extra(
        is_public=True,
        arche_prop="hasAlternativeTitle",
    )
    text_lang = models.CharField(
        max_length=250,
        blank=True,
        default='lat',
        verbose_name="Sprache des Textes",
        help_text="Spraches des Textes, default 'lat'",
    ).set_extra(
        is_public=True,
        arche_prop="hasLanguage",
    )
    jahrhundert = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Jahrundert",
        help_text="Jahrhundert",
    ).set_extra(
        is_public=True,
        data_lookup="tjh",
    )
    start_date = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="von",
        help_text="von",
    ).set_extra(
        is_public=True,
        data_lookup="tzeitvon",
    )
    end_date = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="bis",
        help_text="bis",
    ).set_extra(
        is_public=True,
        data_lookup="tzeitbis",
    )
    edition = models.CharField(
        max_length=350,
        blank=True,
        verbose_name="Edition",
        help_text="Edition",
    ).set_extra(
        is_public=True,
        data_lookup="tedition1",
    )
    art = models.ForeignKey(
        SkosConcept,
        related_name='rvn_text_art_skosconcept',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Textart",
        help_text="Textart",
    ).set_extra(
        is_public=True,
        data_lookup="tart1",
    )
    ort = models.ManyToManyField(
        "Ort",
        related_name='rvn_text_ort_ort',
        blank=True,
        verbose_name="Ort",
        help_text="Ort",
    ).set_extra(
        is_public=True,
        data_lookup="tort",
    )
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="tkommentar",
        arche_prop="hasNote",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'title',
        ]
        verbose_name = "Text"

    def __str__(self):
        if self.title:
            return "{}".format(self.title)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:text_browse')

    @classmethod
    def get_source_table(self):
        return "text"

    @classmethod
    def get_natural_primary_key(self):
        return "legacy_pk"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:text_create')

    def get_absolute_url(self):
        return reverse('archiv:text_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:text_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:text_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:text_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:text_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Event(models.Model):
    title = models.CharField(
        max_length=250,
        blank=True, null=True,
        verbose_name="Titel",
        help_text="Titel des Events"
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Beschreibung",
        help_text="Beschreibung"
    )
    start_date = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="von",
        help_text="von",
    ).set_extra(
        is_public=True,
    )
    end_date = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="bis",
        help_text="bis",
    ).set_extra(
        is_public=True,
    )
    written_date = models.CharField(
        max_length=250,
        blank=True, null=True,
        verbose_name="Datum",
        help_text="z.B. 'um 750'"
    )
    use_case = models.ManyToManyField(
        "UseCase",
        related_name='has_event',
        blank=True,
        verbose_name="Use Case",
        help_text="Verwendet in Use Case",
    ).set_extra(
        is_public=True
    )

    class Meta:

        ordering = [
            'title',
        ]
        verbose_name = "Event"

    def __str__(self):
        return f"{self.title}"

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:event_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:event_create')

    def get_absolute_url(self):
        return reverse('archiv:event_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:event_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:event_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:event_detail',
                kwargs={'pk': prev.first().id}
            )
        return False
