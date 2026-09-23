from django.urls import path
from django.views.generic.base import RedirectView
from django_spaghetti.views import Plate

from . import views

app_name = "webpage"

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    path(
        "data-model",
        Plate.as_view(plate_template_name="webpage/data_model.html"),
        name="data_model",
    ),
    path("", views.GenericWebpageView.as_view(), name="start"),
    path("project-info/", views.project_info, name="project_info"),
    path("<slug:template>", views.GenericWebpageView.as_view(), name="staticpage"),
]
