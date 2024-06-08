from rest_framework import serializers

from apps.courses.models import Course, BoxingCourse, KarateCourse, CyclingCourse, CardioCourse, MeditationCourse, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'instructor',
            'duration'
        ]


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'instructor',
            'duration'
        ]


class BoxingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxingCourse
        fields = [
            'punch_types',
            'sparring_partner_required',

        ]


class BoxingCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxingCourse
        fields = [
            'punch_types',
            'sparring_partner_required',
        ]


class KarateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarateCourse
        fields = [
            'belt_colors',
            'kata_required',

        ]


class KarateCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarateCourse
        fields = [
            'belt_colors',
            'kata_required',

        ]


class CyclingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyclingCourse
        fields = [
            'terrain_type',
            'bike_type',
        ]



class CyclingCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyclingCourse
        fields = [
            'terrain_type',
            'bike_type',

        ]


class CardioCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardioCourse
        fields = [
            'intensity_level',
            'equipment_needed',

        ]


class CardioCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardioCourse
        fields = [
            'intensity_level',
            'equipment_needed',

        ]


class MeditationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationCourse
        fields = [
            'meditation_style',
            'relaxation_techniques',

        ]


class MeditationCourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationCourse
        fields = [
            'meditation_style',
            'relaxation_techniques',

        ]


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'user',
            'course',
            'enrollment_date',

        ]


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'user',
            'course',
            'enrollment_date',
        ]
