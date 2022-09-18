from django.contrib import admin
from django.urls import path,include
from newproj import views

urlpatterns = [
    path("",views.index,name="home"),
    path("bmi",views.bmi,name="bmi"),
    path("about",views.about,name="about"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("register",views.register,name="register"),
    path("details",views.details,name="details"),
    path("bodyindex",views.bodyindex,name="bodyindex"),
    path("diet",views.diet,name="diet"),
    path("settime",views.settime,name="settime"),
    path("showdiet",views.showdiet,name="showdiet"),
    path("foodpyramid",views.foodpyramid,name="foodpyramid"),
    path("viewusers",views.viewusers,name="viewusers"),
    path("bodyweight",views.bodyweight,name="bodyweight"),
    path("viewcharts",views.viewcharts,name="viewcharts"),
    path("healthy",views.healthy,name="healthy"),
    path("obese",views.obese,name="obese"),
    path("overweight",views.overweight,name="overweight"),

]