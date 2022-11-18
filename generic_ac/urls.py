from django.urls import path

from . import views

app_name = 'archiv'
urlpatterns = [
    path(
        '',
        views.generic_ac_view,
        name='generic_ac'
    ),
    path(
        'describe',
        views.describe,
        name='describe'
    ),
]
