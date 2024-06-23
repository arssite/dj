from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    if request.method=="POST": 
        data=request.POST
        #print(data)
        fname=data.get("fname",'DefaultName')
        state=data.get("state","")
        email=data.get("email","")
        city=data.get("city",'Unknown')
        zip=data.get("zip",0)
        image=request.FILES.get("image")
        subject=data.get("subject")
        address=data.get("address","")
        
        
        user = User(fname=fname, address=address, city=city, state=state, zip=zip, subject=subject, image=image)
        user.save()
        return redirect('/')
    return render(request,'contact.html')
