from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerialzier


class ReviewApiViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzier
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(review_owner=self.request.user)
