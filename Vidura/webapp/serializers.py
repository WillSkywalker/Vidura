from django.contrib.auth.models import User
from rest_framework import serializers
from .models import SimulatedConversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class SimulatedConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulatedConversation
        fields = ['id', 'dietary_preference', 'favorite_foods', 'timestamp']
