from django.http import JsonResponse
from django.views.generic.detail import DetailView

from .models import Story


class StoryJsonData(DetailView):
    model = Story

    def render_to_response(self, context, **kwargs):
        data = self.object.payload
        return JsonResponse(data)
