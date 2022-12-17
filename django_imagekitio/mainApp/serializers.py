from rest_framework import serializers
from .models import *

class PhotographersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographers
        fields = '__all__'

class ImagekitAuthSerializer(serializers.Serializer):
   token = serializers.CharField()
   expire = serializers.CharField()
   signature = serializers.CharField()