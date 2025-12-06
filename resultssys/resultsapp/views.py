from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import *
from .schools_selector import(get_schools,get_school)
from .student_selector import(get_students, get_student)

# Create your views here

# HOME PAGE
def manage_iple(request):
    
    context={
        
    }
    return render(request, 'resultsapp/index.html', context)


# SCHOOLS
def manage_schools(request):

    get_all_schools = get_schools()
    
    context={
        "get_all_schools":get_all_schools,
        
    }
    return render(request, 'resultsapp/schools.html', context)
   

# PASSSLIP PAGE
def manage_passslip(request):
    
    context={
        
    }
    return render(request, 'resultsapp/pass_slip.html', context)

# STUDENTS PAGE
def manage_student_in_students(request):

    get_all_students = get_students()
    
    context={
        "get_all_schools":get_all_students,
        
    }
    
# REGISTRATION

def manage_registration(request):
    
    context={
        
    }
    return render(request, 'resultsapp/registration.html', context)

# ABOUT US

def manage_about_us(request):
    
    context={
        
    }
    return render(request, 'resultsapp/about_us.html', context)