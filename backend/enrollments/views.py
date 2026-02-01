from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Enrollment, LessonProgress
from .serializers import EnrollmentSerializer, LessonProgressSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)

    def create(self, request):
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user,
            course_id=request.data['course']
        )
        serializer = self.get_serializer(enrollment)
        return Response(serializer.data)


class LessonProgressViewSet(viewsets.ModelViewSet):
    serializer_class = LessonProgressSerializer

    def get_queryset(self):
        return LessonProgress.objects.filter(enrollment__user=self.request.user)
