from rest_framework.viewsets import ModelViewSet

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerialzier


class ReviewApiViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzier
