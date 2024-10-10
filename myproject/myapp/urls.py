from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import youtubeViewSet

router = DefaultRouter()
router.register('youtube', youtubeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

