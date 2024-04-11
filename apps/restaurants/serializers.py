from rest_framework import serializers

from apps.restaurants.models import Restaurant
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerialzier


class RestaurantSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField(read_only=True)
    arithmetic_mean_estimate = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Restaurant
        read_only_fields = (
            'owner',
        )
        fields = (
            'id',
            'title',
            'latitude',
            'longitude',
            'description',
            'review_count',
            'arithmetic_mean_estimate',
            'reviews',
        )

    def get_arithmetic_mean_estimate(self, obj):
        reviews = Review.objects.filter(restaurant=obj.id)
        lst_of_stars = [review.star for review in reviews]
        estimate = sum(lst_of_stars) / len(lst_of_stars)
        return estimate

    def get_review_count(self, obj):
        reviews = Review.objects.filter(restaurant=obj.id)
        return reviews.count()

    def get_reviews(self, obj):
        reviews = Review.objects.filter(restaurant=obj.id)
        serializer = ReviewSerialzier(reviews, many=True)
        return serializer.data
