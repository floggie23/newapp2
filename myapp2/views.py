from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random

def index(request):
    if "user_id" in request.session :
        return redirect("/order/add")
    return render(request, "index.html")