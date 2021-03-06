from django.conf.urls import url
from . import views
from archiv.endpoint_views import KeyWordEndpoint


app_name = 'archiv'
urlpatterns = [
    url(
        r'^usecase/$',
        views.UseCaseListView.as_view(),
        name='usecase_browse'
    ),
    url(
        r'^usecase/detail/(?P<pk>[0-9]+)$',
        views.UseCaseDetailView.as_view(),
        name='usecase_detail'
    ),
    url(
        r'^usecase/create/$',
        views.UseCaseCreate.as_view(),
        name='usecase_create'
    ),
    url(
        r'^usecase/edit/(?P<pk>[0-9]+)$',
        views.UseCaseUpdate.as_view(),
        name='usecase_edit'
    ),
    url(
        r'^usecase/delete/(?P<pk>[0-9]+)$',
        views.UseCaseDelete.as_view(),
        name='usecase_delete'),
    url(
        r'^usecase-timetable-data/(?P<pk>[0-9]+)$',
        views.get_usecase_timetable_json,
        name='usecase_timetable_json'),
    url(
        r'^spatialcoverage/$',
        views.SpatialCoverageListView.as_view(),
        name='spatialcoverage_browse'
    ),
    url(
        r'^spatialcoverage/detail/(?P<pk>[0-9]+)$',
        views.SpatialCoverageDetailView.as_view(),
        name='spatialcoverage_detail'
    ),
    url(
        r'^spatialcoverage/create/$',
        views.SpatialCoverageCreate.as_view(),
        name='spatialcoverage_create'
    ),
    url(
        r'^spatialcoverage/edit/(?P<pk>[0-9]+)$',
        views.SpatialCoverageUpdate.as_view(),
        name='spatialcoverage_edit'
    ),
    url(
        r'^spatialcoverage/delete/(?P<pk>[0-9]+)$',
        views.SpatialCoverageDelete.as_view(),
        name='spatialcoverage_delete'),
    url(
        r'^autor/$',
        views.AutorListView.as_view(),
        name='autor_browse'
    ),
    url(
        r'^autor/detail/(?P<pk>[0-9]+)$',
        views.AutorDetailView.as_view(),
        name='autor_detail'
    ),
    url(
        r'^autor/create/$',
        views.AutorCreate.as_view(),
        name='autor_create'
    ),
    url(
        r'^autor/edit/(?P<pk>[0-9]+)$',
        views.AutorUpdate.as_view(),
        name='autor_edit'
    ),
    url(
        r'^autor/delete/(?P<pk>[0-9]+)$',
        views.AutorDelete.as_view(),
        name='autor_delete'),
    url(
        r'^keyword/$',
        views.KeyWordListView.as_view(),
        name='keyword_browse'
    ),
    url(
        r'^keyword-data/$',
        KeyWordEndpoint.as_view(),
        name='keyword_data'
    ),
    url(
        r'^cone-data/$',
        KeyWordEndpoint.as_view(),
        name='keyword_data'
    ),
    url(
        r'^keyword/detail/(?P<pk>[0-9]+)$',
        views.KeyWordDetailView.as_view(),
        name='keyword_detail'
    ),
    url(
        r'^keyword/create/$',
        views.KeyWordCreate.as_view(),
        name='keyword_create'
    ),
    url(
        r'^keyword/edit/(?P<pk>[0-9]+)$',
        views.KeyWordUpdate.as_view(),
        name='keyword_edit'
    ),
    url(
        r'^keyword/delete/(?P<pk>[0-9]+)$',
        views.KeyWordDelete.as_view(),
        name='keyword_delete'),
    url(
        r'^ort/$',
        views.OrtListView.as_view(),
        name='ort_browse'
    ),
    url(
        r'^ort/detail/(?P<pk>[0-9]+)$',
        views.OrtDetailView.as_view(),
        name='ort_detail'
    ),
    url(
        r'^ort/create/$',
        views.OrtCreate.as_view(),
        name='ort_create'
    ),
    url(
        r'^ort/edit/(?P<pk>[0-9]+)$',
        views.OrtUpdate.as_view(),
        name='ort_edit'
    ),
    url(
        r'^ort/delete/(?P<pk>[0-9]+)$',
        views.OrtDelete.as_view(),
        name='ort_delete'),
    url(
        r'^stelle/$',
        views.StelleListView.as_view(),
        name='stelle_browse'
    ),
    url(
        r'^stelle/detail/(?P<pk>[0-9]+)$',
        views.StelleDetailView.as_view(),
        name='stelle_detail'
    ),
    url(
        r'^stelle/create/$',
        views.StelleCreate.as_view(),
        name='stelle_create'
    ),
    url(
        r'^stelle/edit/(?P<pk>[0-9]+)$',
        views.StelleUpdate.as_view(),
        name='stelle_edit'
    ),
    url(
        r'^stelle/delete/(?P<pk>[0-9]+)$',
        views.StelleDelete.as_view(),
        name='stelle_delete'),
    url(
        r'^text/$',
        views.TextListView.as_view(),
        name='text_browse'
    ),
    url(
        r'^text/detail/(?P<pk>[0-9]+)$',
        views.TextDetailView.as_view(),
        name='text_detail'
    ),
    url(
        r'^text/create/$',
        views.TextCreate.as_view(),
        name='text_create'
    ),
    url(
        r'^text/edit/(?P<pk>[0-9]+)$',
        views.TextUpdate.as_view(),
        name='text_edit'
    ),
    url(
        r'^text/delete/(?P<pk>[0-9]+)$',
        views.TextDelete.as_view(),
        name='text_delete'),
    url(
        r'^event/$',
        views.EventListView.as_view(),
        name='event_browse'
    ),
    url(
        r'^event/detail/(?P<pk>[0-9]+)$',
        views.EventDetailView.as_view(),
        name='event_detail'
    ),
    url(
        r'^event/create/$',
        views.EventCreate.as_view(),
        name='event_create'
    ),
    url(
        r'^event/edit/(?P<pk>[0-9]+)$',
        views.EventUpdate.as_view(),
        name='event_edit'
    ),
    url(
        r'^event/delete/(?P<pk>[0-9]+)$',
        views.EventDelete.as_view(),
        name='event_delete'
    ),
]
