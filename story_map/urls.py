from django.urls import path

from . import views

app_name = "story_map"

urlpatterns = [
    path("data/<int:pk>/", views.StoryJsonData.as_view()),
]
