from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "webpage"

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    path("", views.GenericWebpageView.as_view(), name="start"),
    path("<slug:template>", views.GenericWebpageView.as_view(), name="staticpage"),
]
