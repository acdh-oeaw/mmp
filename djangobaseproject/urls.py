from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from vocabs import api_views
from archiv import api_views as archiv_api_views
from topics import api_views as topics_api_views

router = routers.DefaultRouter()
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skoscollections', api_views.SkosCollectionViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'autor', archiv_api_views.AutorViewSet)
router.register(r'keyword', archiv_api_views.KeyWordViewSet)
router.register(r'ort', archiv_api_views.OrtViewSet)
router.register(r'ort-geojson', archiv_api_views.GeoJsonOrtViewSet, basename='ort-geojson')
router.register(r'fuzzy-ort-geojson', archiv_api_views.FuzzyGeoJsonOrtViewSet, basename='fuzzy-ort-geojson')
router.register(r'stelle', archiv_api_views.StelleViewSet)
router.register(r'text', archiv_api_views.TextViewSet)
router.register(r'spatialcoverage', archiv_api_views.SpatialCoverageViewSet)
router.register(r'cones', archiv_api_views.ConeViewSet, basename='cones-geojson')
router.register(
    r'lines-and-points',
    archiv_api_views.SpatialCoverageGroupViewSet,
    basename='lines-and-points'
)
router.register(r'usecase', archiv_api_views.UseCaseViewSet)
router.register(r'topics', topics_api_views.TopicViewSet)
router.register(r'text-topic-relation', topics_api_views.TextTopicRelationViewSet)
router.register(r'modeling-process', topics_api_views.ModelingProcessViewSet)
router.register(r'stories', archiv_api_views.StoryViewSet)
router.register(r'slides', archiv_api_views.SlideViewSet)

urlpatterns = [
    path('api/', include(router.urls), name="api-root"),
    path('api-docs/', include_docs_urls(title='MMP-API')),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    path('admin/', admin.site.urls),
    path('browsing/', include('browsing.urls', namespace='browsing')),
    path('story-maps/', include('story_map.urls', namespace='story_map')),
    path('netvis/', include('netvis.urls', namespace="netvis")),
    path('info/', include('infos.urls', namespace='info')),
    path('archiv/', include('archiv.urls', namespace='archiv')),
    path('archiv-ac/', include('archiv.dal_urls', namespace='archiv-ac')),
    path('vocabs/', include('vocabs.urls', namespace='vocabs')),
    path('vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    path('', include('webpage.urls', namespace='webpage')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('openapi', get_schema_view(
        title="MMP",
        description="Mapping Medieval Peoples",
        version="0.1.0"
    ), name='openapi-schema'),
]


handler404 = 'webpage.views.handler404'
