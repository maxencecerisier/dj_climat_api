from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, ClimateImpactViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'climate_impact', ClimateImpactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
