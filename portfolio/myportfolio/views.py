from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from django.http import HttpResponse
import re
from django.contrib import messages
import os
import dotenv 
dotenv.read_dotenv()


# Create your views here.
def Homepage(request):
    return render(request, 'html/index.html')
def Aboutpage(request):
    return render(request, 'html/about.html')

def Contactpage(request):
    if request.method == 'POST' or None:
        name = request.POST.get('name')
        from_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        nameErrs = []
        emailErrs = []
        if not re.match(r"^[a-zA-Z]+(([',. -_][a-zA-Z ])?[a-zA-Z]*)*$", name):
            nameErrs.append('Enter a valid name')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', from_email):
            emailErrs.append('Enter a valid email address')
        if nameErrs or emailErrs:
            return render(request, 'html/contact.html', {'nameErrs':nameErrs, 'emailErrs':emailErrs})
        if name and from_email and subject and message:
            try:
                send_mail(
                    subject,
                    f'Name: {name}\nEmail: {from_email}\nMessage: {message}',
                    from_email,
                    [os.getenv('ADMIN_EMAIL')],
                    fail_silently=False,
                )
                messages.success(request, 'Form was submitted successfully')
            except BadHeaderError:
                return HttpResponse('invalid BadHeader format')
        else:
            return render(request, 'html/contact.html')
    return render(request, 'html/contact.html') 

def Myprojects(request):
    project = Project.objects.all()
    data = {'project':project}
    return render(request, 'html/portfolio.html',data)
def Myresume(request):
    return render(request, 'html/resume.html')




