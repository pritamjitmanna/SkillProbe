from django.shortcuts import render



def index(request):
    return render(request,'homeSite/basic.html')

def signIn(request):

    return render(request,'homeSite/signIn.html')

def signUp(request):

    return render(request,'homeSite/signUp.html')