from django.shortcuts import render,redirect,HttpResponse
from django.http import request
from .forms import loginform

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=="GET":
        form = loginform()
        return render(request,'login.html',{'form':form})
    return redirect('home')

# def blogs_list(request):
#     sort=blogs.objects.all().order_by('-post_date')