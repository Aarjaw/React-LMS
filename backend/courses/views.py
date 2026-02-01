from rest_framework import viewsets, permissions
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True)

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
