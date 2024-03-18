from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .forms import Model_Form

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!!!")

def get_path(request):
    path = request.path
    return HttpResponse(path)

def dish_desc(request, dish):
    text = {
        'pasta' : 'An italian dish',
        'burger' : 'my favourite dish'
    }

    return HttpResponse(f"<h1>{dish}</h1> <p>{text[dish]}</p>")

def form(request):
    context = {"form": forms.demoForm}
    return render(request, 'form.html', context)

def model_form(request):
    form = Model_Form()
    if request.method =="POST":
        form = Model_Form(request.POST)
        if form.is_valid:
            form.save()
    context = {"form": form}
    return render(request, 'form.html', context)