from django.contrib import messages
from django.shortcuts import render, redirect
from App.models import CourseModel, StudentModel


def index(request):
    courseQueryset = CourseModel.objects.all()
    studentQueryset = StudentModel.objects.all()
    return render(request, 'index.html',{"course":courseQueryset,'student':studentQueryset})


def addCourse(request):
    courseQueryset = CourseModel.objects.all()
    studentQueryset = StudentModel.objects.all()
    return render(request,'index.html',{"course":courseQueryset,'student':studentQueryset})


def saveCourse(request):
    courseId=request.POST.get('t1')
    courseName=request.POST.get('t2')
    print(courseName,courseId)
    CourseModel(courseId=courseId,courseName=courseName).save()
    messages.success(request,"Course is Saved")
    return render(request,'index.html',{'course':CourseModel.objects.all(),'student':StudentModel.objects.all()})


def saveStudent(request):
    studentId = request.POST.get('s1')
    studentName = request.POST.get('s2')
    courses = request.POST.getlist('cnames')
    print(studentId,studentName,courses)
    std=StudentModel(studentId=studentId,studentName=studentName)
    std.save()
    std.courseId.set(courses)
    messages.success(request, "Student is Saved")
    return render(request, 'index.html', {'course': CourseModel.objects.all(), 'student': StudentModel.objects.all()})