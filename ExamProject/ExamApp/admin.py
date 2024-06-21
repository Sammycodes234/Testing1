from django.contrib import admin
from .models import StudentInfo,CurrentExam,Courses,Registered_Courses
# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(CurrentExam)
admin.site.register(Courses)
admin.site.register(Registered_Courses)
