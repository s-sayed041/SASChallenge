from django.shortcuts import render
from django.http import HttpResponse


# HOME PAGE
# DESCRIPTION: Select filters for event ideas
#def home(request):
#    context_dict = {}
#
#    #response = render(request, 'planner/home.html', context_dict)
#    return request

def home(request):
    return HttpResponse("Rango says hey there partner!")


# SLOT MACHINE PAGE
# DESCRIPTION: Randomly selects event ideas from given filters
#def slotmachine(request):
#    context_dict = {}
#
#    #response = render(request, 'planner/slotmachine.html', context_dict)
#    return request

def slotmachine(request):
    return HttpResponse("Rango says hey there partner!")