import os

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting



# Create your views here.
def index(request):
    name = input("what is your name? ")
    return HttpResponse('Hello! ' + name)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

