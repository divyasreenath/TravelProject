from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from pyexpat.errors import messages


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['password1']
        if password==Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            if User.objects.filter(username=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

            user.save();
        else:
            print("user created")
            messages.info(request,"password not matching")

    return render(request,"register.html")