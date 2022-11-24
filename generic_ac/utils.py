from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


def query(q, config):
    counter = 0
    response = {"q": q, "next": None, "previous": None, "results": []}
    for x in config:
        or_condition = Q()
        app_name = x["app_name"].lower()
        model_name = x["model_name"].lower()
        model = ContentType.objects.get(
            app_label=app_name, model=model_name
        ).model_class()
        for search_field in x["search_fields"]:
            or_condition.add(Q(**{f"{search_field}__icontains": q}), Q.OR)
        for obj in model.objects.filter(or_condition).distinct():
            counter += 1
            item = {
                "id": obj.id,
                "kind": model_name,
                "app_name": app_name,
                "label": obj.__str__(),
            }
            try:
                item["url"] = obj.get_absolute_url()
            except AttributeError:
                item["url"] = None
            response["results"].append(item)
    response["count"] = counter
    return response
