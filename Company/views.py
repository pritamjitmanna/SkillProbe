
from django.shortcuts import render


def dashboard(request):

    return render(request,'Company/dashboard.html')

def create_challenge(request):

    return render(request,'Company/CompanyChallenges/create_challenge.html')


def page_challenge(request):

    return render(request,'Company/CompanyChallenges/challenge_page_problems.html')

def add_mcq(request):

    return render(request,'Company/CompanyChallenges/add_mcq.html')

def add_coding(request):

    return render(request,'Company/CompanyChallenges/add_coding.html')
