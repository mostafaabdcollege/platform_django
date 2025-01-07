from django.db import models
from users.models import CustomUser
from colorfield.fields import ColorField

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='lessons/images/', null=True, blank=True)
    video = models.FileField(upload_to='lessons/videos/', null=True, blank=True)
    pdf = models.FileField(upload_to='lessons/pdfs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    students = models.ManyToManyField(CustomUser, related_name='student_lessons', blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title

class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='exercises/images/', null=True, blank=True)
    multiple_choice = models.BooleanField(default=False)
    choice1 = models.CharField(max_length=200, null=True, blank=True)
    choice2 = models.CharField(max_length=200, null=True, blank=True)
    choice3 = models.CharField(max_length=200, null=True, blank=True)
    choice4 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question