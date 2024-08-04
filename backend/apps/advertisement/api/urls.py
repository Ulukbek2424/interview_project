from rest_framework.routers import DefaultRouter
from django.urls import include, path

from apps.advertisement.api.views import AdvertisementViewSet

router = DefaultRouter()
router.register('', AdvertisementViewSet, 'advertisement')

advertisement_urlpatterns = [
    path('api/', include(router.urls))
]
