from django.http import JsonResponse
from django.conf import settings
from .utils import query

GENERIC_AC_CONFIG = getattr(settings, "GENERIC_AC_CONFIG")


def generic_ac_view(request):
    config = []
    q = request.GET.get("q") or ""
    try:
        page_size = int(request.GET.get("page_size", 25))
    except ValueError:
        page_size = 25
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1
    only_those = request.GET.getlist("kind")
    if only_those:
        for x in GENERIC_AC_CONFIG:
            if x["model_name"] in only_those:
                config.append(x)
    else:
        config = GENERIC_AC_CONFIG
    data = query(request, q, config, page_size=page_size, page=page)
    if only_those:
        data["filter_on"] = only_those
    else:
        data["filter_on"] = [x["model_name"] for x in GENERIC_AC_CONFIG]

    return JsonResponse(data, safe=False)


def describe(request):
    return JsonResponse(GENERIC_AC_CONFIG, safe=False)
