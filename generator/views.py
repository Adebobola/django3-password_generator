from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(requests):
    return render(requests, 'generator/home.html')

def about(requests):
    return render(requests, 'generator/about.html')


def password(requests):

    characters = list('abcdefghijklmopqrstuvwxyz')

    if requests.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if requests.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if requests.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(requests.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(requests, 'generator/password.html',{'password':thepassword})
