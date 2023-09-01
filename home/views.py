from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable' : "this is sent",
        'variable2' : "the value is not sent"
    }
    messages.success(request, "Welcome to ICECREAM PAARLOUR!")
    return render(request, 'index.html', context)
    #return HttpResponse("This is Homepage") 

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'service.html')
    # return HttpResponse("This is servicepage")

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent.")
    return render(request, 'contact.html')
    # return HttpResponse("This is contactpage")