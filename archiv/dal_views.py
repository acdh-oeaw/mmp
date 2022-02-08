# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import (
    Autor,
    KeyWord,
    Text,
    Stelle,
    Ort,
    UseCase
)


class AutorAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Autor.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q) |
                Q(name_lat__icontains=self.q) |
                Q(name_en__icontains=self.q) |
                Q(name_fr__icontains=self.q) |
                Q(name_it__icontains=self.q) |
                Q(name_gr__icontains=self.q)
            )
        return qs


class KeyWordAC(autocomplete.Select2QuerySetView):

    def get_result_label(self, item):
        return f"{item.stichwort}, <{item.art}>"

    def get_queryset(self):
        qs = KeyWord.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(stichwort__icontains=self.q) |
                Q(wurzel__icontains=self.q) |
                Q(varianten__icontains=self.q)
            )
        return qs


class Eigenname(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = KeyWord.objects.filter(art="Eigenname")

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(stichwort__icontains=self.q) |
                Q(wurzel__icontains=self.q) |
                Q(varianten__icontains=self.q)
            )
        return qs


class Schlagwort(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = KeyWord.objects.filter(art="Schlagwort")

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(stichwort__icontains=self.q) |
                Q(wurzel__icontains=self.q) |
                Q(varianten__icontains=self.q)
            )
        return qs


class OrtAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Ort.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class StelleAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Stelle.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(zitat__icontains=self.q) |
                Q(text__title__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class TextAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Text.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(title__icontains=self.q)
            )
        return qs


class UseCaseAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = UseCase.objects.all()

        if self.q:
            qs = qs.filter(
                Q(title__icontains=self.q)
            )
        return qs
