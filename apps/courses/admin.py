from django.contrib import admin
from apps.courses.models import (
    Course, BoxingCourse,
    KarateCourse, CyclingCourse,
    CardioCourse, MeditationCourse,
    Enrollment
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'duration')


# @admin.register(BoxingCourse)
# class BoxingCourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'instructor', 'duration', 'punch_types', 'sparring_partner_required')


@admin.register(KarateCourse)
class KarateCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'duration', 'belt_colors', 'kata_required')


@admin.register(CyclingCourse)
class CyclingCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'duration', 'terrain_type', 'bike_type')


@admin.register(CardioCourse)
class CardioCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'duration', 'intensity_level', 'equipment_needed')


@admin.register(MeditationCourse)
class MeditationCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'instructor', 'duration', 'meditation_style', 'relaxation_techniques')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrollment_date')
