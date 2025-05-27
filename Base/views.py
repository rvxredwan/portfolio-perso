from django.shortcuts import render, redirect
from django.contrib import messages
from Base import models
from Base.models import Contact

def landing(request):
    return render(request, 'landing.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        if not (1 < len(name) < 30):
            messages.error(request, 'Length of name should be greater than 2 and less than 30 characters.')
            return render(request, 'home.html')

        if not (1 < len(email) < 30):
            messages.error(request, 'Invalid email, try again.')
            return render(request, 'home.html')

        if not (9 < len(number) < 13):
            messages.error(request, 'Invalid number, please try again.')
            return render(request, 'home.html')

        ins = models.Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
    return render(request, 'home.html')

def oussama(request):
    return render(request, 'oussama.html')  
