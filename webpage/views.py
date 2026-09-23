from copy import deepcopy

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .metadata import PROJECT_METADATA as PM


def get_imprint_url():
    try:
        base_url = settings.ACDH_IMPRINT_URL
    except AttributeError:
        base_url = "https://provide-an-acdh-imprint-url/"
    try:
        redmine_id = settings.REDMINE_ID
    except AttributeError:
        redmine_id = "go-register-a-redmine-service-issue"
    return f"{base_url}{redmine_id}"


class ImprintView(TemplateView):
    template_name = "webpage/imprint.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r = requests.get(get_imprint_url())

        if r.status_code == 200:
            context["imprint_body"] = f"{r.text}"
        else:
            context["imprint_body"] = """
            On of our services is currently not available. Please try it later or write an email to
            acdh@oeaw.ac.at; if you are service provide, make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context


class GenericWebpageView(TemplateView):
    template_name = "webpage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apps"] = settings.INSTALLED_APPS
        return context


def handler404(request, exception):
    return render(request, "webpage/404-error.html", locals())


def project_info(request):
    """
    returns a dict providing metadata about the current project
    """

    info_dict = deepcopy(PM)

    if request.user.is_authenticated:
        pass
    else:
        del info_dict["matomo_id"]
        del info_dict["matomo_url"]
    info_dict["base_tech"] = "django"
    info_dict["framework"] = "djangobaseproject"
    return JsonResponse(info_dict)
