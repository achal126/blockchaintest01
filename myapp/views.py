# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from myapp.forms import LoginForm, blockscreenForm, Check, CreateWine, transferWine
from myapp.models import Login
from django.http import HttpResponse, HttpResponseBadRequest
import blockchain as b

# Create your views here.

def login(request):
    username = "not logged in"
    print username

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            print username
    else:
        MyLoginForm = LoginForm()
    if Login.objects.filter(username=username).exists():
        return render(request, 'blockscreen.html', {"username": username})
    else:
        return HttpResponseBadRequest("username or password is wrong")

def renderwineifo(request):
    MyLoginForm = blockscreenForm(request.POST)
    if request.method == "POST" and 'Add' in request.POST:
        if MyLoginForm.is_valid():
            print "Form is valid"
        else:
            MyLoginForm = LoginForm()
        return render(request, 'CreateWineInfo.html',{})

    elif request.method == "POST" and 'Update' in request.POST:
        if MyLoginForm.is_valid():
            print "Form is valid"
        else:
            MyLoginForm = LoginForm()
        return render(request, 'CreateWineInfo.html', {})

    elif request.method == "POST" and 'Transfer' in request.POST:
        if MyLoginForm.is_valid():
            print "Form is valid"
        else:
            MyLoginForm = LoginForm()
        return render(request, 'TransferWine.html', {})

    elif request.method == "POST" and 'Check' in request.POST:
        if MyLoginForm.is_valid():
            print "Form is valid"
        else:
            MyLoginForm = LoginForm()
        return render(request, 'Check.html', {})
    else:
        return HttpResponseBadRequest("Error")


def check(request):
    WineID = "null"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = Check(request.POST)

        if MyLoginForm.is_valid():
            WineID = MyLoginForm.cleaned_data['WineID']
            print WineID
    else:
        MyLoginForm = LoginForm()
    abc = b.query_chaincode("58e639c72e78b47e4122e375063ecf744a201961d1580e3241624e10b0ab0189d69b39c03273854aafd8b55778d22659924944da6f28fd2edee37147ead0ace7",WineID)

    return render(request, 'CheckWineStatus.html', {"WineStatus": abc})

def createwine(request):
    username = "not logged in"
    print username

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = CreateWine(request.POST)

        if MyLoginForm.is_valid():
            wineid = MyLoginForm.cleaned_data['WineID']
            ownerinfo = MyLoginForm.cleaned_data['OwnerInfo']
    else:
        MyLoginForm = LoginForm()
    abc = b.invoke_chaincode('58e639c72e78b47e4122e375063ecf744a201961d1580e3241624e10b0ab0189d69b39c03273854aafd8b55778d22659924944da6f28fd2edee37147ead0ace7', "CreateWineInfo" , wineid, ownerinfo)
    print abc
    if abc == "OK":
        return render(request, 'blockscreen.html', {})
    else:
        return HttpResponseBadRequest("username or password is wrong")

def transfer(request):
    username = "not logged in"
    print username

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = transferWine(request.POST)

        if MyLoginForm.is_valid():
            wineid = MyLoginForm.cleaned_data['WineID']
            ownerinfo = MyLoginForm.cleaned_data['OwnerInfo']
    else:
        MyLoginForm = LoginForm()
    abc = b.invoke_chaincode('58e639c72e78b47e4122e375063ecf744a201961d1580e3241624e10b0ab0189d69b39c03273854aafd8b55778d22659924944da6f28fd2edee37147ead0ace7', "transfer", wineid, ownerinfo)
    print abc
    if abc == "OK":
        return render(request, 'blockscreen.html', {})
    else:
        return HttpResponseBadRequest("username or password is wrong")