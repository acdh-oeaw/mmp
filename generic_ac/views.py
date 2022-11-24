from django.http import JsonResponse
from django.conf import settings
from .utils import query

GENERIC_AC_CONFIG = getattr(settings, "GENERIC_AC_CONFIG")


def generic_ac_view(request):
    config = []
    q = request.GET.get("q") or ""
    only_those = request.GET.getlist("kind")
    if only_those:
        for x in GENERIC_AC_CONFIG:
            if x["model_name"] in only_those:
                config.append(x)
    else:
        config = GENERIC_AC_CONFIG
    data = query(q, config)
    if only_those:
        data["filter_on"] = only_those
    else:
        data["filter_on"] = [x["model_name"] for x in GENERIC_AC_CONFIG]

    return JsonResponse(data, safe=False)


def describe(request):
    return JsonResponse(GENERIC_AC_CONFIG, safe=False)
