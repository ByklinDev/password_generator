from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
def home(request):
    return render(request, 'generator\home.html')

def password(request):
    charachters = list('qwertyuiopasdfghjklzxcvbnm')
    thepassw = ''
    lenpassw = int(request.GET.get('lenght'))
    if request.GET.get('uppercase'):
        charachters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        charachters.extend(list('0123456789'))
    for _ in range(lenpassw):
        thepassw +=  choice(charachters)
    return render(request, 'generator\password.html',{'password':thepassw})

def about(request):
    templ = 'generator\\about.html'
    return render(request, templ)
