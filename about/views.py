from django.shortcuts import render
from django.http import HttpResponse
from .models import About

def about_view(request):
    about_content = About.objects.first()
    return render(request, 'about.html', {'about': about_content})
