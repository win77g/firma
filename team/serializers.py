from .models import *
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name','image','slug','description')


