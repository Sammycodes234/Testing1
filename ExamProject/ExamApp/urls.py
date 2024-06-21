from django.urls import path
from . import views
urlpatterns = [
 
    # These Urls below is a new project
    path("",views.ExamLogin,name="ExamLogin"),
    path("Dashboard",views.Dashboard,name="Dashboard"),
    path("Announcement",views.Announcement,name="Announcement"),
    path("Testrun",views.Testrun,name="Testrun"),
    path("Exam Information",views.ExamInfo,name="ExamInfo"),
    path("Admin Page",views.Admin,name="Admin_Page"),
    path("Student Registration",views.StudentRegistration,name="StudentRegistration"),
    path("matricfunc",views.Username_Check,name="UsernameCheck"),
    path("Student Exam",views.AdminExamInfo,name="AdminExamInfo"),
    path("AdminExamFunc",views.AdminExamFunc,name="AdminExamFunc"),
    path("My Information",views.ProfileInformation,name="ProfileInformation"),
    path("My Profile",views.AdminProfile,name="AdminProfile"),
    path("Upload Courses",views.UploadCourse,name="UploadCourse"),
    path("UploadF..unc",views.UploadFunc,name="UploadFunc"),
    path("Course Registration",views.CourseRegistration,name="CourseRegistration"),
    path('CourseRegFunc',views.CourseRegFunc,name='CourseRegFunc'),
    path("course_get_func",views.courses_get_func,name="courses_get"),
    path("registered_course",views.registered_course_func,name="reg_func"),
    
    path("Logout",views.Logged_Out,name="Logged_Out")

                                                                   
]
