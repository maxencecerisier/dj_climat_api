from rest_framework import serializers
from .models import Users, ClimateImpact

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ClimateImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateImpact
        fields = '__all__'
