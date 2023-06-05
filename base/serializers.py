from rest_framework import serializers
from .models import Agents, Blog

class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

