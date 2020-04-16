from django.contrib import admin
from App.models import CourseModel, StudentModel

class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseId','courseName')


admin.site.register(CourseModel,CourseAdmin)
# admin.site.register(StudentModel)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentId', 'studentName')
admin.site.register(StudentModel, StudentAdmin)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
# admin.site.register(Book, BookAdmin)
