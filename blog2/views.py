from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json


def index(request):
    return render(request,'blog2/index.html')


