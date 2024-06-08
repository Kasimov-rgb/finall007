from django.urls import path
from apps.courses.views import CourseListView, EnrollCourseView

urlpatterns = [
    path('classes', CourseListView.as_view(), name='classes'),
    path('enroll/<int:course_id>/', EnrollCourseView.as_view(), name='enroll_course'),
]
