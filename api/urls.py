from django.urls import include
from django.urls import path

from django.views.generic import TemplateView

from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.views import AuthorViewSet
from api.views import PublisherViewSet
from api.views import BookViewSet

schema_view = get_schema_view(
    title='Books API',
    description='A simple API that lists books.',
    version='1.0.0',
    renderer_classes=[JSONOpenAPIRenderer])

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='api/redoc.html',
            extra_context={'schema_url': 'schema'}),
        name='redoc'),
    path('api/', include(router.urls)),
    path('schema/', schema_view, name="schema"),
]
