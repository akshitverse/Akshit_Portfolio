from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from firstapp.models import Contact
from django.contrib import messages
import re               # re stands for Redirect Expression, it's a build-in python module used to pattern matching in string

# Create your views here.
def index(request):
    #return HttpResponse("This is home page")
    return render(request,'index.html')

def about(request):
    #return HttpResponse("This is about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc =  request.POST.get('desc')

        # Appling validations

        # Check if any field is empty
        if not all([name,email,phone,desc]):
            messages.error(request,"All fields are required.")
            return redirect('contact')

        # Validate phone is of 10 digits
        if not phone.isdigit() or len(phone) != 10:
            messages.error(request,"Phone number must be exactly 10 digits.")
            return render(request,'contact.html',{
                'name': name,
                'email': email,
                'desc': desc
            })
        
        # Checking no number repeats more than 4 times consecutively 
        if re.search(r'(\d)\1{4,}',phone):
            messages.error(request,"Phone number cannot have a digit repeated more than 4 times in a row.")
            return render(request,'contact.html',{
                'name': name,
                'email': email,
                'desc': desc
            })

        # Save contact form data
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your form submitted successfully!")
        return redirect('contact') 
    return render(request,'contact.html')

def projects(request):
    #return HttpResponse("This is contact page")
    return render(request,'projects.html')

def internship(request):
    return render(request,'internship.html')
