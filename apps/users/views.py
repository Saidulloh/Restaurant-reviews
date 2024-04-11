from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import UserSerializer
from apps.restaurants.models import Restaurant
from apps.restaurants.serializers import RestaurantSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerialzier
from utils.Permissions import IsOwner


User = get_user_model()

class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=['get']
    )
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=['get']
    )
    def my_restaurants(self, request):
        restaurants = Restaurant.objects.filter(owner=request.user)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=['get']
    )
    def my_reviews(self, request):
        reviews = Review.objects.filter(review_owner=request.user)
        serializer = ReviewSerialzier(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
