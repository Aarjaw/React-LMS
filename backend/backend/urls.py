from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, CategoryViewSet
from lessons.views import LessonViewSet
from enrollments.views import EnrollmentViewSet, LessonProgressViewSet
from quizzes.views import QuizViewSet, QuizAttemptViewSet
from reviews.views import ReviewViewSet
from certificates.views import CertificateViewSet
from payments.views import PaymentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'progress', LessonProgressViewSet, basename='progress')
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'quiz-attempts', QuizAttemptViewSet, basename='quiz-attempt')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'certificates', CertificateViewSet, basename='certificate')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
