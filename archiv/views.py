# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from . filters import (
    UseCaseListFilter,
    SpatialCoverageListFilter,
    AutorListFilter,
    KeyWordListFilter,
    OrtListFilter,
    StelleListFilter,
    TextListFilter,
    EventListFilter
)
from . forms import (
    AutorForm,
    KeyWordForm,
    OrtForm,
    StelleForm,
    TextForm,
    SpatialCoverageForm,
    UseCaseForm,
    AutorFilterFormHelper,
    KeyWordFilterFormHelper,
    OrtFilterFormHelper,
    StelleFilterFormHelper,
    TextFilterFormHelper,
    SpatialCoverageFilterFormHelper,
    UseCaseFilterFormHelper,
    EventFilterFormHelper,
    EventForm
)
from . tables import (
    AutorTable,
    KeyWordTable,
    OrtTable,
    StelleTable,
    TextTable,
    SpatialCoverageTable,
    UseCaseTable,
    EventTable
)
from . models import (
    Autor,
    KeyWord,
    Ort,
    Stelle,
    Text,
    SpatialCoverage,
    UseCase,
    Event
)
from browsing.browsing_utils import (
    GenericListView, BaseCreateView, BaseUpdateView, BaseDetailView
)


class UseCaseCreate(BaseCreateView):

    model = UseCase
    form_class = UseCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UseCaseCreate, self).dispatch(*args, **kwargs)


class UseCaseUpdate(BaseUpdateView):

    model = UseCase
    form_class = UseCaseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UseCaseUpdate, self).dispatch(*args, **kwargs)


class UseCaseDetailView(BaseDetailView):

    model = UseCase
    template_name = 'archiv/usecase_detail.html'


class UseCaseListView(GenericListView):

    model = UseCase
    filter_class = UseCaseListFilter
    formhelper_class = UseCaseFilterFormHelper
    table_class = UseCaseTable
    init_columns = [
        'id', 'title', 'principal_investigator'
    ]
    enable_merge = False


class UseCaseDelete(DeleteView):

    model = UseCase
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:usecase_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UseCaseDelete, self).dispatch(*args, **kwargs)


def get_usecase_timetable_json(response, pk):
    item = get_object_or_404(UseCase, pk=pk)
    data = item.get_timetable_data()
    return JsonResponse(data, safe=False)


class SpatialCoverageCreate(BaseCreateView):

    model = SpatialCoverage
    form_class = SpatialCoverageForm
    template_name = 'archiv/generic_create.html'

    def get_initial(self):
        initial = super(SpatialCoverageCreate, self).get_initial()
        stelle_id = self.request.GET.get('stelle', None)
        stichwort_id = self.request.GET.get('stichwort', None)
        try:
            stelle_obj = Stelle.objects.get(id=int(stelle_id))
        except (TypeError, ValueError, ObjectDoesNotExist):
            stelle_obj = False
        try:
            stichwort_obj = KeyWord.objects.get(id=int(stichwort_id))
        except (TypeError, ValueError, KeyWord.DoesNotExist):
            stichwort_obj = False
        if stelle_obj:
            initial['stelle'] = self.request.GET.get('stelle', None)
        if stichwort_obj:
            initial['key_word'] = self.request.GET.get('stichwort', None)
        return initial

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SpatialCoverageCreate, self).dispatch(*args, **kwargs)


class SpatialCoverageUpdate(BaseUpdateView):

    model = SpatialCoverage
    form_class = SpatialCoverageForm
    template_name = 'archiv/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SpatialCoverageUpdate, self).dispatch(*args, **kwargs)


class SpatialCoverageDetailView(BaseDetailView):

    model = SpatialCoverage
    template_name = 'archiv/generic_detail.html'


class SpatialCoverageListView(GenericListView):

    model = SpatialCoverage
    filter_class = SpatialCoverageListFilter
    formhelper_class = SpatialCoverageFilterFormHelper
    table_class = SpatialCoverageTable
    init_columns = [
        'id', 'stelle', 'key_word',
    ]
    enable_merge = False
    template_name = 'archiv/spatial_list.html'


class SpatialCoverageDelete(DeleteView):
    model = SpatialCoverage
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:spatialcoverage_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SpatialCoverageDelete, self).dispatch(*args, **kwargs)


class AutorListView(GenericListView):

    model = Autor
    filter_class = AutorListFilter
    formhelper_class = AutorFilterFormHelper
    table_class = AutorTable
    init_columns = [
        'id', 'name',
    ]
    enable_merge = False


class AutorDetailView(BaseDetailView):

    model = Autor
    template_name = 'archiv/generic_detail.html'


class AutorCreate(BaseCreateView):

    model = Autor
    form_class = AutorForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorCreate, self).dispatch(*args, **kwargs)


class AutorUpdate(BaseUpdateView):

    model = Autor
    form_class = AutorForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorUpdate, self).dispatch(*args, **kwargs)


class AutorDelete(DeleteView):
    model = Autor
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:autor_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AutorDelete, self).dispatch(*args, **kwargs)


class KeyWordListView(GenericListView):

    model = KeyWord
    filter_class = KeyWordListFilter
    formhelper_class = KeyWordFilterFormHelper
    table_class = KeyWordTable
    init_columns = [
        'id', 'stichwort', 'wurzel', 'varianten'
    ]
    enable_merge = False
    template_name = 'archiv/keyword_list.html'


class KeyWordDetailView(BaseDetailView):

    model = KeyWord
    template_name = 'archiv/generic_detail.html'


class KeyWordCreate(BaseCreateView):

    model = KeyWord
    form_class = KeyWordForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordCreate, self).dispatch(*args, **kwargs)


class KeyWordUpdate(BaseUpdateView):

    model = KeyWord
    form_class = KeyWordForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordUpdate, self).dispatch(*args, **kwargs)


class KeyWordDelete(DeleteView):
    model = KeyWord
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:keyword_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(KeyWordDelete, self).dispatch(*args, **kwargs)


class OrtListView(GenericListView):

    model = Ort
    filter_class = OrtListFilter
    formhelper_class = OrtFilterFormHelper
    table_class = OrtTable
    init_columns = [
        'id', 'name', 'long', 'lat'
    ]
    enable_merge = False


class OrtDetailView(BaseDetailView):

    model = Ort
    template_name = 'archiv/generic_detail.html'


class OrtCreate(BaseCreateView):

    model = Ort
    form_class = OrtForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrtCreate, self).dispatch(*args, **kwargs)


class OrtUpdate(BaseUpdateView):

    model = Ort
    form_class = OrtForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrtUpdate, self).dispatch(*args, **kwargs)


class OrtDelete(DeleteView):
    model = Ort
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:ort_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrtDelete, self).dispatch(*args, **kwargs)


class StelleListView(GenericListView):

    model = Stelle
    filter_class = StelleListFilter
    formhelper_class = StelleFilterFormHelper
    table_class = StelleTable
    init_columns = [
        'id', 'display_label',
    ]
    enable_merge = False


class StelleDetailView(BaseDetailView):

    model = Stelle
    template_name = 'archiv/stelle_detail.html'


class StelleCreate(BaseCreateView):

    model = Stelle
    form_class = StelleForm
    template_name = 'archiv/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StelleCreate, self).dispatch(*args, **kwargs)


class StelleUpdate(BaseUpdateView):

    model = Stelle
    form_class = StelleForm
    template_name = 'archiv/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StelleUpdate, self).dispatch(*args, **kwargs)


class StelleDelete(DeleteView):
    model = Stelle
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:stelle_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StelleDelete, self).dispatch(*args, **kwargs)


class TextListView(GenericListView):

    model = Text
    filter_class = TextListFilter
    formhelper_class = TextFilterFormHelper
    table_class = TextTable
    init_columns = [
        'id', 'title',
    ]
    enable_merge = False


class TextDetailView(BaseDetailView):

    model = Text
    template_name = 'archiv/generic_detail.html'


class TextCreate(BaseCreateView):

    model = Text
    form_class = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextCreate, self).dispatch(*args, **kwargs)


class TextUpdate(BaseUpdateView):

    model = Text
    form_class = TextForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextUpdate, self).dispatch(*args, **kwargs)


class TextDelete(DeleteView):
    model = Text
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:text_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TextDelete, self).dispatch(*args, **kwargs)


class EventListView(GenericListView):

    model = Event
    filter_class = EventListFilter
    formhelper_class = EventFilterFormHelper
    table_class = EventTable
    init_columns = [
        'id', 'title',
    ]
    enable_merge = False


class EventDetailView(BaseDetailView):

    model = Event
    template_name = 'archiv/event_detail.html'


class EventCreate(BaseCreateView):

    model = Event
    form_class = EventForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreate, self).dispatch(*args, **kwargs)


class EventUpdate(BaseUpdateView):

    model = Event
    form_class = EventForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdate, self).dispatch(*args, **kwargs)


class EventDelete(DeleteView):
    model = Event
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:event_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDelete, self).dispatch(*args, **kwargs)
