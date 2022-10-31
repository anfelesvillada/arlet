from django.urls import path
from .views import (CourseListView, CourseUpdateView, CourseDeleteView, CourseCreateView)

urlpatterns = [   
    path("", CourseListView.as_view(), name="course_list"),
    path("course/new/", CourseCreateView.as_view(), name="course_new"),
    path("course/<int:pk>/edit/", CourseUpdateView.as_view(), name="course_edit"),
    path("course/<int:pk>/delete/", CourseDeleteView.as_view(), name="course_delete")
]