from django.shortcuts import render , HttpResponse
from datetime import datetime
from App.models import contact as c
from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,'index.html')
    #return HttpResponse("This is Home page")

    


def about(request):
    return render(request,'about.html') 

def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact1 = c( name = name, phone = phone, email = email, desc = desc, date = datetime.today())
        contact1.save()

        messages.success(request, 'Your message has been sent successfully.') 

    return render(request,'contact.html')