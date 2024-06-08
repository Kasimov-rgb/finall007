from rest_framework import generics, viewsets
from rest_framework.response import Response

from apps.courses.api.serializers import (
    CourseSerializer, CourseCreateSerializer,
    BoxingCourseSerializer, BoxingCourseCreateSerializer,
    KarateCourseSerializer, KarateCourseCreateSerializer,
    CyclingCourseSerializer, CyclingCourseCreateSerializer,
    CardioCourseSerializer, CardioCourseCreateSerializer,
    MeditationCourseSerializer, MeditationCourseCreateSerializer,
    EnrollmentSerializer, EnrollmentCreateSerializer
)
from apps.courses.models import (
    Course, BoxingCourse, KarateCourse, CyclingCourse,
    CardioCourse, MeditationCourse, Enrollment
)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return CourseCreateSerializer
        elif self.action == 'retrieve':
            return CourseSerializer
        return self.serializer_class


class CourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BoxingCourseViewSet(viewsets.ModelViewSet):
    queryset = BoxingCourse.objects.all()
    serializer_class = BoxingCourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return BoxingCourseCreateSerializer
        elif self.action == 'retrieve':
            return BoxingCourseSerializer
        return self.serializer_class


class BoxingCourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoxingCourse.objects.all()
    serializer_class = BoxingCourseSerializer


class KarateCourseViewSet(viewsets.ModelViewSet):
    queryset = KarateCourse.objects.all()
    serializer_class = KarateCourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return KarateCourseCreateSerializer
        elif self.action == 'retrieve':
            return KarateCourseSerializer
        return self.serializer_class


class KarateCourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KarateCourse.objects.all()
    serializer_class = KarateCourseSerializer
class CyclingCourseViewSet(viewsets.ModelViewSet):
    queryset = CyclingCourse.objects.all()
    serializer_class = CyclingCourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return CyclingCourseCreateSerializer
        elif self.action == 'retrieve':
            return CyclingCourseSerializer
        return self.serializer_class


class CyclingCourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CyclingCourse.objects.all()
    serializer_class = CyclingCourseSerializer


class CardioCourseViewSet(viewsets.ModelViewSet):
    queryset = CardioCourse.objects.all()
    serializer_class = CardioCourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return CardioCourseCreateSerializer
        elif self.action == 'retrieve':
            return CardioCourseSerializer
        return self.serializer_class


class CardioCourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardioCourse.objects.all()
    serializer_class = CardioCourseSerializer


class MeditationCourseViewSet(viewsets.ModelViewSet):
    queryset = MeditationCourse.objects.all()
    serializer_class = MeditationCourseSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return MeditationCourseCreateSerializer
        elif self.action == 'retrieve':
            return MeditationCourseSerializer
        return self.serializer_class


class MeditationCourseUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeditationCourse.objects.all()
    serializer_class = MeditationCourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return EnrollmentCreateSerializer
        elif self.action == 'retrieve':
            return EnrollmentSerializer
        return self.serializer_class


class EnrollmentUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
