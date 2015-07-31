import os

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse

from hello.models import posts

from .models import Greeting

# Create your views here.
def index(request):
    return render_to_response('test.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})