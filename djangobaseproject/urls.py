from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from vocabs import api_views
from archiv import api_views as archiv_api_views

router = routers.DefaultRouter()
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skoscollections', api_views.SkosCollectionViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'authors', archiv_api_views.AutorViewSet)
router.register(r'autor', archiv_api_views.AutorViewSet)
router.register(r'edition', archiv_api_views.EditionViewSet)
router.register(r'keyword', archiv_api_views.KeyWordViewSet)
router.register(r'ort', archiv_api_views.OrtViewSet)
router.register(r'stelle', archiv_api_views.StelleViewSet)
router.register(r'text', archiv_api_views.TextViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
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
