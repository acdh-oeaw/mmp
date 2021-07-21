from django.views.generic.list import ListView
from django.http import JsonResponse

from archiv.models import KeyWord
from archiv.filters import KeyWordListFilter
from archiv.network_utils import create_graph, graph_table


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
