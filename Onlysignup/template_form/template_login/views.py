from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def template_login(request):
    return render(request,'login.html')
def template_signup(request):
    if request.method=="POST": 
        data=request.POST
        #print(data)
        first_name=data.get("first_name")
        email=data.get("email")
        password=data.get("password")
        username=data.get("username")
        
        user=User.objects.create(
            first_name=first_name,email=email,username=username
        )
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request,'signup.html')