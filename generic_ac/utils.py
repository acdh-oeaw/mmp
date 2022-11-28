from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q


def query(request, q, config, page_size=5, page=1):
    current_url = f"{request.build_absolute_uri()}"
    base_url = request.get_host()
    if f"page={page}" in current_url:
        pass
    else:
        current_url = f"{current_url}&page={page}"
    total_count = 0
    response = {
        "q": q,
        "page_size": page_size,
        "next": None,
        "previous": None,
        "count": None,
        "results": [],
    }
    for x in config:
        or_condition = Q()
        app_name = x["app_name"].lower()
        model_name = x["model_name"].lower()
        model = ContentType.objects.get(
            app_label=app_name, model=model_name
        ).model_class()
        for search_field in x["search_fields"]:
            or_condition.add(Q(**{f"{search_field}__icontains": q}), Q.OR)
        qs = model.objects.filter(or_condition).distinct()
        total_count += qs.count()
        p = Paginator(model.objects.filter(or_condition).distinct(), page_size)
        try:
            p.page(page)
            has_objects = True
        except EmptyPage:
            has_objects = False
        if has_objects:
            for obj in p.page(page).object_list:
                item = {
                    "id": obj.id,
                    "additional_fields": None,
                    "kind": model_name,
                    "app_name": app_name,
                    "label": obj.__str__(),
                }
                try:
                    item["url"] = f"{base_url}{obj.get_absolute_url()}"
                except AttributeError:
                    item["url"] = None
                if x.get("additional_fields"):
                    item["additional_fields"] = {}
                    for key, value in x["additional_fields"].items():
                        extra_fields = {
                            "label": value["label"],
                            "data": f'{getattr(obj, value["lookup"])}'
                        }
                        item["additional_fields"][key] = extra_fields
                response["results"].append(item)
    response["count"] = total_count
    if total_count > page_size * page:
        response["next"] = current_url.replace(f"page={page}", f"page={page + 1}")
    if page > 1:
        response["previous"] = current_url.replace(f"page={page}", f"page={page - 1}")
    return response
