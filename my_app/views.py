from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos" : Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojo.objects.create(name=request.POST["name"], city=request.POST["city"], state=request.POST["state"])
    return redirect("/")

def add_ninja(request):
    my_dojo = Dojo.objects.get(id = request.POST["dojo_id"])
    Ninja.objects.create(first_name=request.POST["first_name"], last_name = request.POST["last_name"], dojo = my_dojo )
    return redirect("/")
