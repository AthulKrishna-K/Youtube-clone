from rest_framework import serializers
from .models import youtube

class youtubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = youtube
        fields = '__all__'
