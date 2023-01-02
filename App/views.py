from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        terms = request.POST.get('terms')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.terms = terms

        contact.save()
        messages.success(request, "The message was sent successefully !")
        context = {
            "contact": contact,
            "messages": messages
        }
        return render(request,"home.html")
    return render(request,"home.html")