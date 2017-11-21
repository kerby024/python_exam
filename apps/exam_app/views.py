# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User
from .models import Message

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'exam_app/index.html')

def register(request):
    errors = User.objects.registration_validation(request.POST)
    if request.method == 'POST':
        User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email_address = request.POST['email'])
    request.session['name'] = request.POST['name']
    return redirect ('/display')

def addquote(request):
    # Message.objects.registration_validation(request.POST)
    if request.method == 'POST':
        Message.objects.create(
            author = request.POST['author'],
            message = request.POST['message'])
    return redirect('/addquote')

def display(request):
    context = {
        'users' :User.objects.all(),
        'messages' :Message.objects.all()
    }
    return render(request, 'exam_app/display.html', context)
# Create your views here.
