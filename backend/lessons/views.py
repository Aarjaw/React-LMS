from rest_framework import viewsets
from .models import Lesson
from .serializers import LessonSerializer

class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        course_id = self.request.query_params.get('course')
        return Lesson.objects.filter(course_id=course_id)
