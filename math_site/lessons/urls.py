from django.urls import path
from . import views
urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('create/', views.create_lesson, name='create_lesson'),
    path('create_exercise/', views.create_exercise, name='create_exercise'),
    path('lesson/<int:pk>/edit/', views.edit_lesson, name='edit_lesson'),
    path('lesson/<int:pk>/delete/', views.delete_lesson, name='delete_lesson'),
    path('lessons/create/', views.create_lesson, name='create_lesson'),
    path('dashboard/', views.dashboard, name='dashboard'),
]