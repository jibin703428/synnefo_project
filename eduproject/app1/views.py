from django.shortcuts import render
from .models import task

def index(request):
    p=task.objects.all()
    return render(request,"todo.html", {"s":p})
