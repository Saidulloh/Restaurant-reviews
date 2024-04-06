from rest_framework import serializers

from apps.restaurants.models import Restaurant
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerialzier


class RestaurantSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'title',
            'latitude',
            'longitude',
            'description',
            'reviews',
        )

    def get_reviews(self, obj):
        reviews = Review.objects.filter(restaurant=obj.id)
        serializer = ReviewSerialzier(reviews, many=True)
        return serializer.data
