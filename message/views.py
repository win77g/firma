from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from message.serializers import *
# Create your views here.

# сериализация сообщения
class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
# Create your views here.
