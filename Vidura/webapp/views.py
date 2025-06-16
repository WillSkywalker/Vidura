from rest_framework import viewsets, permissions
from django.db.models import Q
from django.contrib.auth.models import User
from .models import SimulatedConversation, DietaryPreference
from .serializers import SimulatedConversationSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VegetarianVeganFoodViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimulatedConversationSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):

        return SimulatedConversation.objects.filter(
            Q(dietary_preference=DietaryPreference.VEGETARIAN) |
            Q(dietary_preference=DietaryPreference.VEGAN)
        ).order_by('-timestamp')


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimulatedConversationSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        return SimulatedConversation.objects.order_by('-timestamp')
