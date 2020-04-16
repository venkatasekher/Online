from django.db import models


class CourseModel(models.Model):
    courseId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=32)

    # def __str__(self):
    #     return self.courseName


class StudentModel(models.Model):
    studentId = models.IntegerField(primary_key=True)
    studentName = models.CharField(max_length=32)
    courseId = models.ManyToManyField(CourseModel)

    def __str__(self):
        return self.studentName
