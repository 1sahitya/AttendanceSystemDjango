from django.urls import path
from .views import (SubjectView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
                    CourseView, CourseCreateView, CourseUpdateView, CourseDeleteView,
                    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView)


urlpatterns = [
    path('subject/', SubjectView.as_view(), name='subject'),
    path('subject/new/', SubjectCreateView.as_view(), name='subject-create'),
    path('subject/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject-update'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject-delete'),
    path('course/', CourseView.as_view(), name='course'),
    path('course/new/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('student/', StudentListView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('studnet/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete')
]
