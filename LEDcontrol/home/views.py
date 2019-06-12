# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as gpio

# Create your views here.

def index(request):
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(11, gpio.LOW)
    selected = request.POST.get('led', False)
    print(selected)

    if selected == 'on':
        gpio.output(11, True)
    else:
        gpio.output(11, False)
        
    context = {'selected': selected,}
    return render(request, 'home/index.html', context)
    #return HttpResponse('<h1> welcome </h1>')
    
