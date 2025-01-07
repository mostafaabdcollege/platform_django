from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson, Exercise
from .forms import LessonForm, ExerciseForm

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    exercises = Exercise.objects.filter(lesson=lesson)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'exercises': exercises})

@login_required
def create_lesson(request):
    if request.user.user_type != 'teacher':
        return redirect('lesson_list')
    
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = request.user
            lesson.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'lessons/create_lesson.html', {'form': form})

@login_required
def create_exercise(request):
    if request.user.user_type != 'teacher':
        return redirect('lesson_list')
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = ExerciseForm()
    return render(request, 'lessons/create_exercise.html', {'form': form})

@login_required
def edit_lesson(request, pk):
    if request.user.user_type != 'teacher':
        return redirect('lesson_list')
    
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lessons/edit_lesson.html', {'form': form, 'lesson': lesson})

@login_required
def delete_lesson(request, pk):
    if request.user.user_type != 'teacher':
        return redirect('lesson_list')
    
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    return render(request, 'lessons/delete_lesson.html', {'lesson': lesson})

@login_required
def dashboard(request):
    lesson_count = Lesson.objects.count()
    exercise_count = Exercise.objects.count()
    context = {
        'lesson_count': lesson_count,
        'exercise_count': exercise_count,
    }
    return render(request, 'lessons/dashboard.html', context)