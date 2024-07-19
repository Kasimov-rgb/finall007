# from django.shortcuts import render, redirect
# from django.views import View, generic
# from apps.courses.models import Course, Enrollment
# from django.contrib.auth.decorators import login_required
# from apps.courses.forms import EnrollmentForm

# from apps.courses.models import Course, CreateView, CourseForm, reverse_lazy, UpdateView, DeleteView


# class CourseListView(generic.ListView):
#     model = Course
#     template_name = 'salud/classes.html'
#     context_object_name = 'classes'


# class EnrollCourseView(View):
#     @login_required
#     def get(self, request, course_id):
#         course = Course.objects.get(pk=course_id)
#         form = EnrollmentForm()
#         return render(request, 'courses/enroll_course.html', {'course': course, 'form': form})

#     @login_required
#     def post(self, request, course_id):
#         course = Course.objects.get(pk=course_id)
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             Enrollment.objects.create(user=request.user, course=course)
#             return redirect('course_list')
#         return render(request, 'courses/enroll_course.html', {'course': course, 'form': form})




# class CourserCreateView(CreateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'course/courses_create.html'
#     success_url = reverse_lazy('courses')

# class CourseUpdateView(UpdateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'course/courses_update.html'
#     success_url = reverse_lazy('course')

# class TrainerDeleteView(DeleteView):
#     model = Course
#     template_name = 'course/ourses_delete.html'
#     success_url = reverse_lazy('trainer')



from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.courses.models import Course, Enrollment
from apps.courses.forms import CourseForm, EnrollmentForm

class CourseListView(generic.ListView):
    model = Course
    template_name = 'salud/classes.html'
    context_object_name = 'classes'

@method_decorator(login_required, name='dispatch')
class EnrollCourseView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        form = EnrollmentForm()
        return render(request, 'course/enroll_course.html', {'course': course, 'form': form})

    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            Enrollment.objects.create(user=request.user, course=course)
            return redirect('classes')
        return render(request, 'courses/enroll_course.html', {'course': course, 'form': form})

@method_decorator(login_required, name='dispatch')
class CourseCreateView(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_create.html'
    success_url = reverse_lazy('classes')

@method_decorator(login_required, name='dispatch')
class CourseUpdateView(generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_update.html'
    success_url = reverse_lazy('classes')

@method_decorator(login_required, name='dispatch')
class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'course/course_delete.html'
    success_url = reverse_lazy('classes')
