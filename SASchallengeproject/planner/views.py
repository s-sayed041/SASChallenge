from django.shortcuts import render
from django.http import HttpResponse
import random

# HOME PAGE
# DESCRIPTION: Select filters for event ideas
#def home(request):
#    context_dict = {}
#
#    #response = render(request, 'planner/home.html', context_dict)
#    return request
recommendations = [
    "Bar","Cinema","Museum","Park","Restaurant","Theatre","Concert","Bowling","Club","Cafe"
]

def home(request):
    results = [random.choice(recommendations) for _ in range(3)]
    return render(request, 'planner/home.html', {'results': results})



# SLOT MACHINE PAGE
# DESCRIPTION: Randomly selects event ideas from given filters
#def slotmachine(request):
#    context_dict = {}
#
#    #response = render(request, 'planner/slotmachine.html', context_dict)
#    return request

def slotmachine(request):
    return HttpResponse("Rango says hey there partner!")