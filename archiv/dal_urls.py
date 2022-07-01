from django.urls import path
from . import dal_views

app_name = 'archiv'
urlpatterns = [
    path(
        'autor-autocomplete/',
        dal_views.AutorAC.as_view(),
        name='autor-autocomplete'
    ),
    path(
        'keyword-autocomplete/',
        dal_views.KeyWordAC.as_view(),
        name='keyword-autocomplete'
    ),
    path(
        'schlagwort-autocomplete/',
        dal_views.Schlagwort.as_view(),
        name='schlagwort-autocomplete'
    ),
    path(
        'ethonym-autocomplete/',
        dal_views.Ethnonym.as_view(),
        name='ethonym-autocomplete'
    ),
    path(
        'region-autocomplete/',
        dal_views.Region.as_view(),
        name='retion-autocomplete'
    ),
    path(
        'eigenname-autocomplete/',
        dal_views.Eigenname.as_view(),
        name='eigenname-autocomplete'
    ),
    path(
        'ort-autocomplete/',
        dal_views.OrtAC.as_view(),
        name='ort-autocomplete'
    ),
    path(
        'stelle-autocomplete/',
        dal_views.StelleAC.as_view(),
        name='stelle-autocomplete'
    ),
    path(
        'text-autocomplete/',
        dal_views.TextAC.as_view(),
        name='text-autocomplete'
    ),
    path(
        'usecase-autocomplete/',
        dal_views.UseCaseAC.as_view(),
        name='usecase-autocomplete'
    ),
]
