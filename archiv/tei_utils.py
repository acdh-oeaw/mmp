import lxml.etree as ET
import re

from django.template.loader import get_template


def get_context(res):
    context = {}
    context['object'] = res
    return context


def get_node_from_template(template_path, res, full=True):
    template = get_template(template_path)
    context = get_context(res)
    context['FULL'] = full
    temp_str = f"{template.render(context=context)}"
    node = ET.fromstring(temp_str)
    return node
