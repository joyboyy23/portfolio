from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('contact:contact')
    
    return render(request, 'contact/contact.html')