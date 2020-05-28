from .models import *
from rest_framework import serializers


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('id','name','category','image','slug','description','description_short')

class CategoryTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTemplate
        fields = ('name',)
