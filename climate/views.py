from rest_framework import viewsets
from .models import Users, ClimateImpact
from .serializers import UsersSerializer, ClimateImpactSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ClimateImpactViewSet(viewsets.ModelViewSet):
    queryset = ClimateImpact.objects.all()
    serializer_class = ClimateImpactSerializer
