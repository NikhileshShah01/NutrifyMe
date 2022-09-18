import re
from django.shortcuts import render,HttpResponse,redirect
from newproj.models import Register
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("this is NutrifyMe home page")
    return render(request,'index.html')

def about(request):
    return render(request,'AboutUs.html')
    # return HttpResponse("this is NutrifyMe about page")

def bmi(request):
    return render(request,'bmi.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get("name")
        age=request.POST.get("age")
        city=request.POST.get("city")
        gender=request.POST.get("gender")
        userid=request.POST.get("userid")
        password=request.POST.get("userpass")
        CREATION=User.objects.create_user(userid,' ',password)
        resgister=Register(name=name,age=age,city=city,
                gender=gender,userid=userid,password=password)
        resgister.save()
        CREATION.save()
        return redirect("/login")
    return render(request,'register.html')

def loginUser(request):
    if request.method=='POST':
        loginid=request.POST.get('loginid')
        loginpassword=request.POST.get('loginpass')    
        user = authenticate(username=loginid, password=loginpassword)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            if loginid=='DBA' and loginpassword=='DBA':
                viewusers(request)
                return redirect("/viewusers")
            else:
                details(request)
                return redirect("/details")
        else:
            messages.info(request, 'Invalid User-Id or password. Please Try again!!')
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'index.html')

def details(request):
    if request.user.is_anonymous:
        return redirect("/")
    curr_user=request.user
    detail=Register.objects.filter(userid=curr_user.username)[0]
    params={'customer':detail}    
    return render(request,'details.html',params)

def bodyindex(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'bmi2.html')

def settime(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':
        breakfast=request.POST.get("breakfast")
        lunch=request.POST.get("lunch")
        snacks=request.POST.get("snacks")
        dinner=request.POST.get("dinner")
        resgister=Register(breakfast=breakfast,lunch=lunch,snacks=snacks,
                dinner=dinner)
        resgister.save()
        return redirect("/showdiet")        
    return render(request,'settime.html')

def showdiet(request):
    if request.user.is_anonymous:
        return redirect("/")
    curr_user=request.user
    detail=Register.objects.filter(userid=curr_user.username)[0]
    params={'customer':detail}        
    return render(request,'showdiet.html',params)

def diet(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'diet.html')

def foodpyramid(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'foodpyramid.html')

def viewusers(request):
    if request.user.is_anonymous:
        return redirect("/")
    detail=Register.objects.all()
    params={'users':detail}    
    return render(request,'viewusers.html',params)

def bodyweight(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'bmi3.html')

def viewcharts(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'viewcharts.html')

def healthy(request):
    if request.user.is_anonymous:
        return redirect("/")
    curr_user=request.user
    detail=Register.objects.filter(userid=curr_user.username)[0]
    params={'customer':detail}        
    return render(request,'healthy.html',params)

def obese(request):
    if request.user.is_anonymous:
        return redirect("/")
    curr_user=request.user
    detail=Register.objects.filter(userid=curr_user.username)[0]
    params={'customer':detail}        
    return render(request,'obese.html',params)

def overweight(request):
    if request.user.is_anonymous:
        return redirect("/")
    curr_user=request.user
    detail=Register.objects.filter(userid=curr_user.username)[0]
    params={'customer':detail}        
    return render(request,'overweight.html',params)