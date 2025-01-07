from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('inspector', 'Inspector'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    student_number = models.CharField(max_length=20, null=True, blank=True)
    teacher_number = models.CharField(max_length=20, null=True, blank=True)
    inspector_number = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures/', null=True, blank=True)