from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Person

def index(request):
    persons = Person.objects.all()[0]
    return render(request,'index.html',{"persons":persons})