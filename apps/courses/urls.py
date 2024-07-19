# from django.urls import path
# from apps.courses.views import CourseListView, EnrollCourseView, CourseDeleteView, CourseUpdateView, CourseCreateView

# urlpatterns = [
#     path('courses/', CourseListView.as_view(), name='classes'),
#     path('enroll/<int:course_id>/', EnrollCourseView.as_view(), name='enroll_course'),


#     path('course/new/', CourseCreateView.as_view(), name='courses_create'),
#     path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='courses_update'),
#     path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='courses_delete'),
# ]



from django.urls import path
from apps.courses.views import CourseListView, EnrollCourseView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='classes'),
    path('enroll/<int:course_id>/', EnrollCourseView.as_view(), name='enroll_course'),
    path('course/new/', CourseCreateView.as_view(), name='courses_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='courses_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='courses_delete'),
]

