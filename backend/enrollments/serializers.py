from rest_framework import serializers
from .models import Enrollment, LessonProgress
from courses.serializers import CourseSerializer
from lessons.serializers import LessonSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'


class LessonProgressSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = LessonProgress
        fields = '__all__'
