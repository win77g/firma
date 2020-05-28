from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from templates.views import TemplateViewSet
from team.views import TeamViewSet
from message.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'template', TemplateViewSet)
router.register(r'team', TeamViewSet)
router.register(r'message', MessageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
