import random
import requests

from django.shortcuts import render
from django.http import HttpResponse

EVENTS = [
    {"name": "The Tipsy Cow", "type": "Food & Drink", "location": "Glasgow City Centre", "mood": "Fun", "budget": "££", "group": "Small", "desc": "Cozy bar with cocktails", "score": 7},
    {"name": "O2 Academy", "type": "Music", "location": "Finnieston", "mood": "Party", "budget": "£££", "group": "Medium", "desc": "Live music concerts", "score": 9},
    {"name": "Escape Glasgow", "type": "Activity", "location": "Merchant City", "mood": "Chill", "budget": "££", "group": "Medium", "desc": "Escape room adventures", "score": 8},
    {"name": "The Stand Comedy Club", "type": "Performing & Visual Arts", "location": "Central", "mood": "Fun", "budget": "£", "group": "Small", "desc": "Stand-up comedy nights", "score": 8},
    {"name": "BrewDog Bar", "type": "Food & Drink", "location": "West End", "mood": "Party", "budget": "££", "group": "Medium", "desc": "Craft beers and lively atmosphere", "score": 8},
    {"name": "Nice N Sleazy", "type": "Music", "location": "City Centre", "mood": "Party", "budget": "£", "group": "Medium", "desc": "Live music and DJ nights", "score": 8},
    {"name": "Kelvingrove Art Gallery", "type": "Performing & Visual Arts", "location": "West End", "mood": "Chill", "budget": "£", "group": "Small", "desc": "Art exhibitions and cultural events", "score": 7},
    {"name": "Go Ape Treemendous Adventure", "type": "Activity", "location": "Pollok Park", "mood": "Fun", "budget": "££", "group": "Medium", "desc": "Outdoor rope courses and adventure", "score": 9},
]


# HOME PAGE
# DESCRIPTION: Select filters for event ideas
def home(request):
    context_dict = {}

    response = render(request, 'planner/home.html', context=context_dict)
    return response


# SLOT MACHINE PAGE
# DESCRIPTION: Randomly selects event ideas from given filters
def slotmachine(request):
        return render(request, "planner/slot.html", {"EVENTS": EVENTS})


def results(request):
    show_all = request.GET.get("show_all")
    randomizer = request.GET.get("random")
    if randomizer:  
       top = [random.choice(EVENTS)] 
    else:  
        mood = request.GET.get("mood")
        budget = request.GET.get("budget")
        group = request.GET.get("group")
        activity_type = request.GET.get("activity_type")
        occasion = request.GET.get("occasion")

        filtered = []
        for e in EVENTS:
            if (not mood or e["mood"] == mood) and \
               (not budget or e["budget"] == budget) and \
               (not group or e["group"] == group) and \
               (not activity_type or e["type"] == activity_type):
                filtered.append(e)
        if show_all:
            top = filtered
        else:
            top = filtered[:5]

    return render(request, "planner/results.html", {"activities": top, "occasion": request.GET.get("occasion", "")})

