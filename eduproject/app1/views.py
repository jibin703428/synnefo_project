from django.shortcuts import render

def index(request):
    return render(request,"home.html")
def index2(reqest):
    return render(reqest,"courses.html")