from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from archiv.models import SpatialCoverage, Stelle


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


@login_required
def copy_stelle(request):
    try:
        current_id = request.GET['current-id']
    except KeyError:
        return redirect('/')
    try:
        item = Stelle.objects.get(id=current_id)
    except (ObjectDoesNotExist, ValueError):
        return redirect('/')
    use_case = item.use_case.all()
    item.id = None
    item.zitat = "###KOPIE###"
    item.summary = "###KOPIE###"
    item.lemmata = None
    item.save()
    item.use_case.set(use_case)
    return redirect(item.get_edit_url())
