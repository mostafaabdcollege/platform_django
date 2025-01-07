from django import forms
from .models import Lesson, Exercise

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'