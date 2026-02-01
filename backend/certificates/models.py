from django.db import models
from accounts.models import User
from courses.models import Course

# Create your models here.

class certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.certificate_id
