from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(course_id=self.request.query_params.get('course'))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
