from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaisViewSet,RegionViewSet

router = DefaultRouter()

router.register(r'pais', PaisViewSet)
router.register(r'region', RegionViewSet)

urlpatterns = [
    path('', include(router.urls))
]