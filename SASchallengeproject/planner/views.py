from django.shortcuts import render

# HOME PAGE
# DESCRIPTION: Select filters for event ideas
def home(request):
    return render(request, 'planner/home.html')

# SLOT MACHINE PAGE
# DESCRIPTION: Randomly selects event ideas from given filters
def slot(request):
    return render(request, 'planner/slot.html')