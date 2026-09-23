from django.urls import path

from archiv.endpoint_views import (
    KeyWordAuthorEndpoint,
    KeyWordEndpoint,
    KeyWordStelle,
    NlpDataStelle,
    StopWordListView,
    get_usecase_timetable_json,
    key_word_by_century,
)

from . import tei_views

app_name = "archiv"
urlpatterns = [
    path("keyword/century/<int:pk>", key_word_by_century, name="keyword_by_century"),
    path("keyword-network/", KeyWordEndpoint.as_view(), name="keyword_data"),
    path(
        "keyword-author-network/", KeyWordAuthorEndpoint.as_view(), name="keyword_data"
    ),
    path("text/xml-tei/<int:pk>", tei_views.text_to_tei, name="text_xml"),
    path("nlp-data/", NlpDataStelle.as_view(), name="nlp_data"),
    path("kw-stelle/", KeyWordStelle.as_view(), name="keyword_stelle"),
    path("stopwords/", StopWordListView.as_view(), name="stopwords"),
    path(
        "usecase-timetable-data/<int:pk>",
        get_usecase_timetable_json,
        name="usecase_timetable_json",
    ),
]
