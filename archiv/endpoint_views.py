from django.views.generic.list import ListView
from django.http import JsonResponse

from archiv.models import KeyWord
from archiv.filters import KeyWordListFilter

from archiv.network_utils import create_graph, graph_table


class KeyWordEndpoint(ListView):

    model = KeyWord
    filter_class = KeyWordListFilter

    def get_queryset(self, **kwargs):
        qs = super(KeyWordEndpoint, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs

    def render_to_response(self, context, **kwargs):
        qs = self.get_queryset()
        if qs.count() < 70:
            df = graph_table(qs)
        else:
            df = graph_table(qs[:70])
        data = create_graph(df, qs)
        return JsonResponse(data)
