
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoViewSet
from django.conf.urls import include
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include(router.urls)),
     path('api-token-auth/', views.obtain_auth_token),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
