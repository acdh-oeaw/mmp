import pandas as pd
from collections import Counter, defaultdict
from django.db.models import Count
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from archiv.models import KeyWord, Text, Stelle
from archiv.filters import KeyWordListFilter, StelleListFilter
from archiv.network_utils import create_graph, graph_table
from archiv.utils import cent_from_year
from archiv.nlp_utils import get_nlp_data

default = [
    [x, 0] for x in range(1, 15)
]


class KeyWordStelle(ListView):

    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordStelle, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset().distinct().order_by('id')
        key_words = [x[0] for x in list(qs.values_list('key_word__stichwort'))]
        key_word_counter = Counter(key_words)
        data = {
            "token_dict":
            [{x[0]: x[1]} for x in key_word_counter.most_common(len(key_words))]
        }
        return JsonResponse(data)


class NlpDataStelle(ListView):

    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super(NlpDataStelle, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset().distinct().order_by('id')
        data = get_nlp_data(qs)
        return JsonResponse(data)


def key_word_by_century(request, pk):
    kw = get_object_or_404(KeyWord, pk=pk)
    props = ['id', 'not_before']
    items = Text.objects.filter(
        rvn_stelle_text_text__key_word=kw, not_before__gte=100, not_after__lte=2000
    ).distinct().order_by('not_before').values_list(*props)
    if items:
        df = pd.DataFrame(items, columns=props)
        df['century_start'] = df.apply(lambda x: cent_from_year(x['not_before']), axis=1)
        data = df.groupby(
            'century_start',
            as_index=False, group_keys=False, sort=False
        ).count()[['century_start', 'id']].values.tolist()
        d = defaultdict(int)
        for k, v in data:
            d[k] = v
        for x in range(1, 16):
            d[x] = d.get(x, 0)
        payload = list(sorted(d.items()))
    else:
        payload = default
    result = {
        'id': pk,
        'title': kw.stichwort,
        'data': payload
    }

    return JsonResponse(result)


class KeyWordEndpoint(ListView):

    model = KeyWord
    filter_class = KeyWordListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordEndpoint, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset().distinct().order_by('id')
        if qs.count() < 100:
            df = graph_table(qs)
        else:
            df = graph_table(qs.reverse()[:500])
        data = create_graph(df, KeyWord)
        return JsonResponse(data)
