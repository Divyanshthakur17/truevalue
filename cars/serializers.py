from .models import NewCars, UsedCars
from rest_framework import serializers

class NewCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCars
        fields = "__all__"

class UsedCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedCars
        fields = "__all__"
        