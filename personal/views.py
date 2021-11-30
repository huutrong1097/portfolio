from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import ContactForm
from django.contrib import messages
from .models import (
    About, 
    Skill,  
    SubSkill,
    Education,
    Contact
)
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipient_list = ['huutrong1097@gmail.com']
            send_mail(user_name , message, email, recipient_list)
            form.save()
            return messages.success(request, 'Your information is sent to candidate!')
        else:
            return messages.error(request, 'Your information is not sent to candidate. Please check again!')
    else:
        form = ContactForm()
        about_me = About.objects.get(name__icontains= 'trong')
        skills = Skill.objects.all()
        subskills = SubSkill.objects.select_related('title').all()
        educations = Education.objects.all()
        context = {
            'about_me': about_me,
            'skills': skills,
            'subskills': subskills,
            'educations': educations,
            'form': form,
        }
    return render(request, 'index.html', context=context)
