from django.shortcuts import render, redirect
from django.views import View
from apps.courses.models import Course, Enrollment
from django.contrib.auth.decorators import login_required
from apps.courses.forms import EnrollmentForm

from apps.courses.models import Course


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'salud/classes.html', {'courses': courses})


class EnrollCourseView(View):
    @login_required
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        form = EnrollmentForm()
        return render(request, 'courses/enroll_course.html', {'course': course, 'form': form})

    @login_required
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            Enrollment.objects.create(user=request.user, course=course)
            return redirect('course_list')
        return render(request, 'courses/enroll_course.html', {'course': course, 'form': form})
