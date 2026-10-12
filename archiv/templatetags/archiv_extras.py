from django import template
from django.utils.html import format_html_join

from archiv.crud_registry import crud

register = template.Library()


@register.simple_tag
def crud_browse_menu_items():
    """Dropdown entries linking to the list view of every model in the crud registry."""
    items = sorted(
        (model._meta.verbose_name_plural.title(), model.get_listview_url())
        for model in crud._registry
    )
    return format_html_join(
        "\n",
        '<li><a class="dropdown-item" href="{}">{}</a></li>',
        ((url, name) for name, url in items),
    )


@register.filter(name="split")
def split(value, key):
    """
    Returns the value turned into a list.
    """
    return value.split(key)
