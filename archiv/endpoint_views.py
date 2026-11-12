from collections import Counter, defaultdict

import pandas as pd
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from archiv.filters import StelleListFilter
from archiv.models import Autor, KeyWord, Stelle, Text, UseCase
from archiv.network_utils import create_graph, graph_table
from archiv.nlp_utils import get_nlp_data
from archiv.utils import cent_from_year
from topics.models import StopWord

default = [[x, 0] for x in range(-3, 16)]


def get_usecase_timetable_json(response, pk):
    item = get_object_or_404(UseCase, pk=pk)
    data = item.get_timetable_data()
    return JsonResponse(data, safe=False)


class StopWordListView(ListView):
    model = StopWord

    def render_to_response(self, context, **kwargs):

        data = {"result": [x[0] for x in StopWord.objects.all().values_list("word")]}
        return JsonResponse(data)


class KeyWordStelle(ListView):
    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct().prefetch_related("key_word")

    def render_to_response(self, context, **kwargs):
        qs = self.object_list.order_by("id")
        key_words = [
            keyword.stichwort for stelle in qs for keyword in stelle.key_word.all()
        ]
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
        qs = super().get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.object_list.order_by("id")
        data = get_nlp_data(qs)
        return JsonResponse(data)


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
    df = pd.DataFrame.from_records(items.iterator(), columns=props)
    if not df.empty:
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
        payload = sorted(d.items())
    else:
        payload = default
    result = {"id": pk, "title": kw.stichwort, "data": payload}

    return JsonResponse(result)


class KeyWordEndpoint(ListView):
    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        qs = self.object_list.order_by("id")
        df = graph_table(qs)
        data = create_graph(df)
        return JsonResponse(data)


class KeyWordAuthorEndpoint(ListView):
    model = Stelle
    filter_class = StelleListFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset().distinct()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs.distinct()

    def render_to_response(self, context, **kwargs):
        author_ids = self.request.GET.getlist("author", [])
        try:
            author_qs = Autor.objects.filter(id__in=author_ids)
        except ValueError:
            author_qs = []
        qs = self.object_list.order_by("id")
        df = graph_table(qs)
        data = create_graph(df)
        node_ids = {x["key"] for x in data["nodes"]}
        if author_qs:
            keywords_by_author = defaultdict(list)
            matching_keywords = (
                KeyWord.objects.filter(
                    rvn_stelle_key_word_keyword__text__autor__in=author_qs,
                    rvn_stelle_key_word_keyword__in=qs,
                )
                .order_by("stichwort")
                .values_list("rvn_stelle_key_word_keyword__text__autor__id", "id")
                .distinct()
            )
            for author_id, keyword_id in matching_keywords:
                keywords_by_author[author_id].append(keyword_id)

            for x in author_qs:
                node = {
                    "key": f"autor_{x.id}",
                    "id": x.id,
                    "kind": "autor",
                    "label": f"{x}",
                }
                data["nodes"].append(node)
                for keyword_id in keywords_by_author[x.id]:
                    kw_id = f"keyword_{keyword_id}"
                    if kw_id in node_ids:
                        data["edges"].append(
                            {
                                "key": f"autor_{x.id}__keyword_{keyword_id}",
                                "source": f"autor_{x.id}",
                                "target": kw_id,
                            }
                        )
        return JsonResponse(data)
