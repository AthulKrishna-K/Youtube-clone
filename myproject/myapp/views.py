from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import youtube
from .serializers import youtubeSerializer

class youtubeViewSet(viewsets.ModelViewSet):
    queryset = youtube.objects.all()
    serializer_class = youtubeSerializer