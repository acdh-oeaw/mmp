# generated by appcreator

from django.db import models
from django.urls import reverse

from vocabs.models import SkosConcept

from browsing.browsing_utils import model_to_dict


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


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


class Edition(models.Model):
    """ Edition """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    zitat = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Zitat",
        help_text="Zitat",
    ).set_extra(
        is_public=True,
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
            'zitat',
        ]
        verbose_name = "Edition"

    def __str__(self):
        if self.zitat:
            return "{}".format(self.zitat)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:edition_browse')

    @classmethod
    def get_source_table(self):
        return None

    @classmethod
    def get_natural_primary_key(self):
        return "zitat"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:edition_create')

    def get_absolute_url(self):
        return reverse('archiv:edition_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:edition_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:edition_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:edition_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:edition_detail',
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
    art = models.CharField(
        max_length=250,
        blank=True,
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
            return "{}".format(self.stichwort)
        else:
            return "{}".format(self.legacy_id)

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
    kommentar = models.TextField(
        blank=True, null=True,
        verbose_name="Kommentar",
        help_text="Kommentar",
    ).set_extra(
        is_public=True,
        data_lookup="skommentar",
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
        verbose_name = "Stelle"

    def __str__(self):
        if self.legacy_pk:
            return "{}".format(self.legacy_pk)
        else:
            return "{}".format(self.legacy_id)

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
    edition = models.ManyToManyField(
        "Edition",
        related_name='rvn_text_edition_edition',
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


