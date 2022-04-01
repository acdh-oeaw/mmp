from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from archiv.models import SpatialCoverage


@login_required
def copy_beleg(request):
    try:
        current_id = request.GET['current-id']
    except KeyError:
        return redirect('/')
    try:
        item = SpatialCoverage.objects.get(id=current_id)
    except (ObjectDoesNotExist, ValueError):
        return redirect('/')
    stellen = item.stelle.all()
    item.id = None
    item.kommentar = f"###KOPIE### {item.kommentar} ###KOPIE### "
    item.save()
    item.stelle.set(stellen)
    return redirect(item.get_edit_url())
