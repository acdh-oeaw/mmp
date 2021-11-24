from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

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
router.register(r'stelle', archiv_api_views.StelleViewSet)
router.register(r'text', archiv_api_views.TextViewSet)
router.register(r'spatialcoverage', archiv_api_views.SpatialCoverageViewSet)
router.register(r'cones', archiv_api_views.ConeViewSet)
router.register(r'usecase', archiv_api_views.UseCaseViewSet)
router.register(r'topics', topics_api_views.TopicViewSet)
router.register(r'text-topic-relation', topics_api_views.TextTopicRelationViewSet)
router.register(r'modeling-process', topics_api_views.ModelingProcessViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('api-docs/', include_docs_urls(title='MMP-API')),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(r'^admin/', admin.site.urls),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^netvis/', include('netvis.urls', namespace="netvis")),
    url(r'^info/', include('infos.urls', namespace='info')),
    url(r'^archiv/', include('archiv.urls', namespace='archiv')),
    url(r'^archiv-ac/', include('archiv.dal_urls', namespace='archiv-ac')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]


handler404 = 'webpage.views.handler404'
