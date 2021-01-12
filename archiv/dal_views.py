# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import *


class AutorAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Autor.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
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


