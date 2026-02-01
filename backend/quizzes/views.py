from rest_framework import viewsets
from .models import Quiz, QuizAttempt
from .serializers import QuizSerializer, QuizAttemptSerializer

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuizSerializer

    def get_queryset(self):
        lesson_id = self.request.query_params.get('lesson')
        return Quiz.objects.filter(lesson_id=lesson_id)


class QuizAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = QuizAttemptSerializer

    def get_queryset(self):
        return QuizAttempt.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
