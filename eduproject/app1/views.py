from django.shortcuts import render,redirect
from app1.models import task


def base(request):
    if request.method=="POST":
        name= request.POST['name']
        task_text = request.POST['task_text']
        t = task( name=name, task_text=task_text)
        t.save()
    p=task.objects.all()
    return render(request,"base.html", {"s":p})




def delete(request,task_id):
    dt= task.objects.get(id=task_id)
    dt.delete()

    return redirect(base)

def edit(request,task_id):
    dt= task.objects.get(id=task_id)
    if request.method=="POST":
        name= request.POST['name']
        task_text = request.POST['task_text']
        task.objects.filter(id=task_id).update( name=name, task_text=task_text)
      
        return redirect(base)
    
    return render(request,"update.html", {"s":dt})
    

    