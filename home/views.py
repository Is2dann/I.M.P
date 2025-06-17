from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def im_home(request):
    return HttpResponse("Welcome to the world of Iceman Media Photography! You'll be able to book sessions once it's ready.")
