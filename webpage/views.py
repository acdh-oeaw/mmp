import requests
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.template.exceptions import TemplateDoesNotExist
from django.views.generic import TemplateView


class ImprintView(TemplateView):
    template_name = "webpage/imprint.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            imprint_url = f"{settings.ACDH_IMPRINT_URL}{settings.REDMINE_ID}"
        except Exception as e:
            context["imprint_body"] = e
            return context
        r = requests.get(imprint_url)
        if r.status_code == 200:
            context["imprint_body"] = f"{r.text}"
        else:
            context["imprint_body"] = """
            On of our services is currently not available.\
            Please try it later or write an email to\
            acdh-ch-helpdesk@oeaw.ac.at; if you are service provide,\
            make sure that you provided ACDH_IMPRINT_URL and REDMINE_ID
            """
        return context


class GenericWebpageView(TemplateView):
    template_name = "webpage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apps"] = settings.INSTALLED_APPS
        return context

    def get_template_names(self):
        template_name = "webpage/{}.html".format(self.kwargs.get("template", "index"))
        try:
            loader.select_template([template_name])
        except TemplateDoesNotExist:
            raise Http404
        return [template_name]


def handler404(request, exception):
    return render(request, "webpage/404-error.html", locals())
