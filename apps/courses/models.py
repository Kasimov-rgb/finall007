from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    instructor = models.CharField(
        max_length=100,
    )
    duration = models.PositiveIntegerField()

    image_for_classes = models.ImageField(
        upload_to="classes_media/",
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title


class BoxingCourse(Course):


    def __str__(self):
        return self.title


class KarateCourse(Course):
    belt_colors = models.CharField(
        max_length=100,
    )
    kata_required = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title


class CyclingCourse(Course):
    terrain_type = models.CharField(
        max_length=100,
    )
    bike_type = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.title


class CardioCourse(Course):
    intensity_level = models.CharField(
        max_length=100,
    )
    equipment_needed = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.title


class MeditationCourse(Course):
    meditation_style = models.CharField(
        max_length=100,
    )
    relaxation_techniques = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
