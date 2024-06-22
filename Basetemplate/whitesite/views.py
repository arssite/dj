from django.shortcuts import render

# Create your views here.
def home(request):
    page="home"
    return render(request,'home.html',context={"context":page})
def contact(request):
    page="contact"
    return render(request,'contact.html',context={"context":page})
def about(request):
    page="about"
    return render(request,'about.html',context={"context":page})