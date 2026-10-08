from browsing.utils import (
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
    GenericFilterFormHelper,
    GenericListView,
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from archiv.models import UseCase


class UseCaseListView(GenericListView):
    model = UseCase
    formhelper_class = GenericFilterFormHelper
    init_columns = ["name", "part_of"]
    enable_merge = False


class UseCaseDetailView(BaseDetailView):
    model = UseCase


class UseCaseCreate(BaseCreateView):
    model = UseCase
    # form_class = UseCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UseCaseUpdate(BaseUpdateView):
    model = UseCase
    # form_class = UseCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UseCaseDelete(DeleteView):
    model = UseCase
    template_name = "webpage/confirm_delete.html"
    success_url = reverse_lazy("archiv:archiv_browse")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
