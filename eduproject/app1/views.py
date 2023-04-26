from django.shortcuts import render,redirect
from app1.models import task


def home(request):
    if request.method=="POST":
        name= request.POST['name']
        task_text = request.POST['task_text']
        t = task( name=name, task_text=task_text)
        t.save()
    
    
    

    p=task.objects.all()
    return render(request,"todo.html", {"s":p})




def delete(request,task_id):
    dt= task.objects.get(id=task_id)
    dt.delete()

    return redirect(home)