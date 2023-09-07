
from django.shortcuts import render


def dashboard(request):

    return render(request,'Candidate/dashboard.html')


def challenge(request):

    return render(request,'Candidate/challenges/challenge.html')


def test_page(request):

    return render(request,'Candidate/challenges/challenge_test_page.html')


def before_time(request):

    return render(request,'Candidate/challenges/before_time_page.html')