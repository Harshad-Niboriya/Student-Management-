from django.shortcuts import render,redirect
from .models import user
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages

def sign_in(request):
    retrun render(request,'index.html')
def sign-up(request):
    return render(request,'sign-up.html')
def (home(request):
    return render(request,'sign-up.html')
def pg_dash(request):
    return render(request,'pg_dashboard.html')
def course(request):
    return render(request,'courses.html')
def dash(request):
    return render(request,'courses.html')
def dash(request):
    return render(request,'dashboard.html')

def sign_up_data(request):
    if request.method=='POST':
            Name=request.POST['User_Name']
            Email=request.POST['User_Email']
            Password=make_password(request.POST['User_Password'])
            user.save()
            return redirect('/''')  
def sign_in_data(request):
    if request.method=='POST':
        Email=request.POST['sign_in_Email']
        password=request.POST['sign_in_password']
        if User.objects.filter(Email=Email)
        password=obj.Password
        if check_password(Password=password):
            return redirect('/dash')
        else:
            return HttpResponse("Passsword incorrect")
    else:
        return HttpResponse("Email is not register")
    
# def courses(request):
#     return render(request,'app/courses.html')
# def dashboard(request):
#     return render(request,'app/dashboard.html')
# def hostel(request):
#     return render(request,'app/hostel_details.html')
# def notice(request):
#     return render(request,'app/notifications.html')





    