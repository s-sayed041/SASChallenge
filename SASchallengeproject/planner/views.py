import random

from django.shortcuts import render
from django.http import HttpResponse


recommendations = ["Bar", "Cinema", "Museum", "Park", "Restaurant", "Theater", "Concert",
                    "Hiking", "Beach", "Amusement Park"]

# HOME PAGE
# DESCRIPTION: Select filters for event ideas
def home(request):
    context_dict = {}

    response = render(request, 'planner/home.html', context=context_dict)
    return response


# SLOT MACHINE PAGE
# DESCRIPTION: Randomly selects event ideas from given filters
def slotmachine(request):
    context_dict = {}
    response = render(request, 'planner/slotmachine.html', context=context_dict)
    return response
