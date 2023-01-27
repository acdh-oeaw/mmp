import pandas as pd
from collections import Counter, defaultdict
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


from archiv.models import KeyWord, Text, Stelle, Autor
from archiv.filters import StelleListFilter
from archiv.network_utils import create_graph, graph_table
from archiv.utils import cent_from_year
from archiv.nlp_utils import get_nlp_data
from topics.models import StopWord


default = [[x, 0] for x in range(-3, 16)]


class StopWordListView(ListView):

    model = StopWord

    def render_to_response(self, context, **kwargs):

        data = {"result": [x[0] for x in StopWord.objects.all().values_list("word")]}
        return JsonResponse(data)


class KeyWordStelle(ListView):

    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordStelle, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset().distinct().order_by("id")
        qs_kw = [x.key_word.all().distinct() for x in qs]
        key_words = []
        for x in qs_kw:
            for y in x:
                key_words.append(y.stichwort)
        key_word_counter = Counter(key_words)
        data = {
            "token_dict": [
                {x[0]: x[1]} for x in key_word_counter.most_common(len(key_words))
            ]
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
        qs = self.get_queryset().distinct().order_by("id")
        data = get_nlp_data(qs)
        clean_token = [x for x in data["token"]]
        clean_data = {
            "token": clean_token,
            "token_dict": dict(Counter(clean_token)),
            "token_count": len(clean_token),
            "unique_token_count": len(set(clean_token)),
        }
        return JsonResponse(clean_data)


def key_word_by_century(request, pk):
    kw = get_object_or_404(KeyWord, pk=pk)
    props = ["id", "not_before"]
    items = (
        Text.objects.filter(
            rvn_stelle_text_text__key_word=kw, not_before__gte=-300, not_after__lte=2000
        )
        .distinct()
        .order_by("not_before")
        .values_list(*props)
    )
    if items:
        df = pd.DataFrame(items, columns=props)
        df["century_start"] = df.apply(
            lambda x: cent_from_year(x["not_before"]), axis=1
        )
        data = (
            df.groupby("century_start", as_index=False, group_keys=False, sort=False)
            .count()[["century_start", "id"]]
            .values.tolist()
        )
        d = defaultdict(int)
        for k, v in data:
            d[k] = v
        for x in range(-3, 16):
            d[x] = d.get(x, 0)
        payload = list(sorted(d.items()))
    else:
        payload = default
    result = {"id": pk, "title": kw.stichwort, "data": payload}

    return JsonResponse(result)


class KeyWordEndpoint(ListView):

    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordEndpoint, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset().distinct().order_by("id")
        df = graph_table(qs)
        data = create_graph(df)
        return JsonResponse(data)


class KeyWordAuthorEndpoint(ListView):

    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordAuthorEndpoint, self).get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        author_ids = self.request.GET.getlist("author", [])
        try:
            author_qs = Autor.objects.filter(id__in=author_ids)
        except ValueError:
            author_qs = []
        qs = self.get_queryset().distinct().order_by("id")
        df = graph_table(qs)
        data = create_graph(df)
        node_ids = [x['key'] for x in data['nodes']]
        if author_qs:
            for x in author_qs:
                node = {
                    "key": f"autor_{x.id}",
                    "id": x.id,
                    "kind": "author",
                    "label": f"{x}",
                }
                data["nodes"].append(node)
                kw = KeyWord.objects.filter(
                    rvn_stelle_key_word_keyword__text__autor=x.id, rvn_stelle_key_word_keyword__in=qs
                ).distinct()
                for e in kw:
                    kw_id = f"keyword_{e.id}"
                    if kw_id in node_ids:
                        data["edges"].append(
                            {
                                "id": f"autor_{x.id}__keyword_{e.id}",
                                "source": f"autor_{x.id}",
                                "target": kw_id,
                            }
                        )
        return JsonResponse(data)
