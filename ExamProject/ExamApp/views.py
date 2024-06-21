from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def ExamLogin(request):
    if request.method == "POST":
        Username=request.POST['username']
        Password=request.POST['password']
        Info=authenticate(username=Username,password=Password)
        if Info is not None:
            login(request,Info)
            try:
               StudentInfo.objects.get(Matric=Username)
               return redirect('Dashboard')
            except:
                return redirect('Admin_Page')
                
        else:
            Context={
            'dflex':"d-flex"
            }  
            return render(request,'Exam Login.html',Context)
        
    else:
        Context={
            'dflex':"d-0"
        }
        return render(request,"Exam Login.html",Context)  
    
    
def Dashboard(request):
    try:
        user=request.user.username
        Info=StudentInfo.objects.get(Matric=user)
        Context={'Student':Info}
        return render(request,"Dashboard.html",Context)
    except:
        return redirect("ExamLogin")
        
def Announcement(request):
    User=request.user.username
    Validity=StudentInfo.objects.get(Matric=User)
    if Validity.Announcement == 'True':
        return HttpResponse("Announcement")
    else:
        return HttpResponse(Validity.Announcement)
  
    
def Testrun(request):
    return render(request,"testrun.html")

def ExamInfo(request):
    try:
        user=request.user.username
        Info=StudentInfo.objects.get(Matric=user)
        Info.Announcement = 'False'
        Info.save()
        try:
            Announcement=CurrentExam.objects.get(Department=Info.Department)
            Announce=1
        except:
            Announcement=''
            Announce=0
            
        
        Context={'Student':Info,
                 'Announcement':Announcement,
                 'Announce':Announce
                 }
        return render(request,"ExamInfo.html",Context)
    except:
        return redirect("ExamLogin")
    
def Admin(request):
    return render(request,"Admin_page.html" )

def StudentRegistration(request):
    if request.method == "POST":
        Names=request.POST["Names"]
        Picture=request.POST['Picture']
        Department=request.POST['Department']
        Date_Of_Birth=request.POST["DOB"]
        Matric=request.POST["Matric"]
        user=User.objects.create_user(username=Matric,password="1234567")
        user.save()
        Student=StudentInfo(FullName=Names,Matric=Matric,Picture=Picture,Department=Department,DOB=Date_Of_Birth,Announcement='False')
        Student.save()
        context={
            "dnone":"d-flex"
        } 
        return render(request,"Student Registration.html",context)
    else:
        context={
            "dnone":"d-none"
        } 
        return render (request,"Student Registration.html",context)
    
def Username_Check(request):
    Matric=request.GET['Matric']
    if StudentInfo.objects.filter(Matric=Matric).exists():
        return HttpResponse("Username Exists")
    else:
        return HttpResponse("Username Available")    
        
        
        
def AdminExamInfo(request):
    return render (request,"AdminExamInfo.html")
def AdminExamFunc(request):
    Department=request.GET['Department']
    Course=request.GET['Course']
    Date=request.GET['Date']
    Venue=request.GET['Venue']
    Time=request.GET['Time']
    Validity=CurrentExam.objects.filter(Department=Department)
    if Validity.exists():
        Validity.delete()
        for x in StudentInfo.objects.all():
            if x.Department == Department:
                x.Announcement = 'True'
                x.save()
            
        Creation=CurrentExam(Department=Department,Course=Course,Venue=Venue,Time=Time,Date=Date)
        Creation.save()
    else:
        for x in StudentInfo.objects.all():
            if x.Department == Department:
                x.Announcement = 'True'
                x.save()
            
        Creation=CurrentExam(Department=Department,Course=Course,Venue=Venue,Time=Time,Date=Date)
        Creation.save()
       
    return HttpResponse("success")

def courses_get_func(request):
    Department=request.GET['Department']
    Course_List=Courses.objects.filter(Department=Department)
    length=len(Course_List)
    return  JsonResponse({'Courses':list(Course_List.values()),"leng":length})
def registered_course_func(request):
    Matric=request.user.username
    Department=StudentInfo.objects.get(Matric=Matric)
    Department=Department.Department
    course=request.GET['course']
    if Registered_Courses.objects.filter(Department=Department,Matric=Matric,Course=course).exists():
        return HttpResponse("success")
    else:
        return HttpResponse("Error")
def ProfileInformation(request):
    try:
        User=request.user.username
        Info=StudentInfo.objects.get(Matric=User)
        Context={   'Student':Info   }
        return render (request,"Profile Information.html",Context)
    except:
        return redirect("ExamLogin")
    
def AdminProfile(request):
    return render(request,"Admin Profile.html")

def CourseRegistration(request):
    try:
        User=request.user.username
        Users=StudentInfo.objects.get(Matric=User)
        context={"Student":Users,
                 'Courses':Courses.objects.all()
                 
                 }
        return render(request,"Course Registration.html",context)
    except:
        return redirect("ExamLogin")
def CourseRegFunc(request):
    User=request.user.username
    Department=StudentInfo.objects.get(Matric=User)
    Department=Department.Department
    Course=request.GET['Course']
    
    if Registered_Courses.objects.filter(Matric=User,Course=Course).exists():
        Existing=Registered_Courses.objects.get(Matric=User,Course=Course)
        Existing.delete()
        return HttpResponse("Error")
    else:
        Course_Registration=Registered_Courses(Matric=User,Course=Course,Department=Department)
        Course_Registration.save()
        return HttpResponse("Success")
    
    
    
def UploadCourse(request):
    
    return render(request,"CourseUpload.html" )       

def UploadFunc(request):
    Department=request.GET['Department']
    CourseCode=request.GET['CourseCode']
    CourseTitle=request.GET['CourseTitle']
    Upload=Courses(Course_Title=CourseTitle,Department=Department,Course_Code=CourseCode) 
    Upload.save()
   
    return HttpResponse("success")    

def Logged_Out(request):
    logout(request)
    return redirect("ExamLogin")
