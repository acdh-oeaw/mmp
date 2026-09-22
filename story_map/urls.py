from django.urls import path
from . import views

app_name = 'story_map'

urlpatterns = [
    path('<int:pk>/', views.StoryDetailView.as_view()),
    path('data/<int:pk>/', views.StoryJsonData.as_view()),
]
