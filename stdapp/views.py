from django.shortcuts import render,redirect
from stdapp.models import Course,Student
from .models import Student

# Create your views here.


def home(request):
    return render(request,'home.html')

def coursedetails(request):
    return render(request,'course.html')

def studadd(request):
    return render(request,'studadd.html')

def showstudent(request):
    return render(request,'showstudent.html')
def add_coursedb(request):
    if request.method=="POST":
        course_name=request.POST.get('coursename')
        course_fee=request.POST.get('coursefee')
        course=Course(coursename=course_name,coursefee=course_fee)
        course.save()
        return redirect('/')
def studadd(request):
    courses=Course.objects.all()
    return render(request,'studadd.html',{'course':courses})      

def add_studentdb(request):
    if request.method=="POST":
        student_name=request.POST['studentname']
        student_address=request.POST['address']
        student_age=request.POST['age']
        joinig_date=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(studentname=student_name,address=student_address,age=student_age,jdate=joinig_date,course=course1)
        student.save()
        return redirect('showstudent')
def show_details(request):
    student=Student.objects.all()
    return render(request,'showstudnt.html',{'students':student})    
def showstudent(request):
    student=Student.objects.all()
    return render(request,'showstudent.html',{'students':student})

    
def edit(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'student':student,'course':course})

def editdb(request,pk):
    if request.method=="POST":
       students=Student.objects.get(id=pk)
       students.studentname=request.POST['studentname']
       students.address=request.POST['address']
       students.age=request.POST['age']
       students.jdate=request.POST['jdate']
       
       sel=request.POST['sel']
       
       course1=Course.objects.get(id=sel)
       students.course=course1
       students.save()
       return redirect('showstudent')
    
def delete(request,pk):
    d =Student.objects.get(id=pk)
    d.delete()
    return redirect('showstudent')