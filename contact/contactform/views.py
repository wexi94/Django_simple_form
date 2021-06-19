from django.shortcuts import render
from .models import ContactForm

def index(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contactform = ContactForm(name=name, email=email, password=password)
        contactform.save()
    return render(request, 'index.html')