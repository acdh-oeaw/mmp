from browsing.utils import (
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
    GenericFilterFormHelper,
    GenericListView,
)
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CrudRegistry:
    """Registers a model and builds its browse/detail/create/edit/delete views and urls."""

    def __init__(self):
        self._registry = {}

    def register(self, model, **list_options):
        """Extra keyword arguments (e.g. init_columns) become attributes of the list view."""
        name = model.__name__

        def build(suffix, bases, **attrs):
            return type(f"{name}{suffix}", bases, {"model": model, **attrs})

        views = {
            "browse": build(
                "ListView",
                (GenericListView,),
                formhelper_class=GenericFilterFormHelper,
                **list_options,
            ),
            "detail": build("DetailView", (BaseDetailView,)),
            "create": build("Create", (LoginRequiredMixin, BaseCreateView)),
            "edit": build("Update", (LoginRequiredMixin, BaseUpdateView)),
            "delete": build(
                "Delete",
                (LoginRequiredMixin, DeleteView),
                template_name="webpage/confirm_delete.html",
                success_url=model.get_listview_url(),
            ),
        }
        self._registry[model] = views
        return views

    def get_urls(self):
        patterns = []
        for model, views in self._registry.items():
            base = model._get_url_basename()
            routes = {
                "browse": f"{base}/",
                "detail": f"{base}/detail/<int:pk>",
                "create": f"{base}/create/",
                "edit": f"{base}/edit/<int:pk>",
                "delete": f"{base}/delete/<int:pk>",
            }
            for action, route in routes.items():
                patterns.append(
                    path(route, views[action].as_view(), name=f"{base}_{action}")
                )
        return patterns


crud = CrudRegistry()
