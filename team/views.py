from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from team.serializers import *


# сериаизация заголовка
class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # filter_fields = ('category',)
