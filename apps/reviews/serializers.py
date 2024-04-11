from rest_framework import serializers

from apps.reviews.models import Review


class ReviewSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Review
        read_only_fields = (
            'review_owner',
        )
        fields = (
            'id',
            'comment',
            'star',
            'restaurant',
        )
