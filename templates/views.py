from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from templates.serializers import *


# сериаизация заголовка
class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    filter_fields = ('category',)

# class NewsFromCategoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     filter_fields = ('category',)
#
# # Create your views here.
