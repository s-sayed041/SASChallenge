import os
import random
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

EVENTBRITE_SEARCH_URL = "https://www.eventbriteapi.com/v3/events/search/"

@api_view(['GET'])
def events_search(request):
    # filters from query params
    location = request.GET.get('location')
    price = request.GET.get('price')   # "free" or "paid" or absent
    alcohol = request.GET.get('alcohol')  # "true" to search alcohol keywords
    category = request.GET.get('category')  # optional Eventbrite category id

    params = {
        'expand': 'venue,logo',
    }
    if location:
        params['location.address'] = location
    if price:
        params['price'] = price  # Eventbrite expects 'free' or 'paid'
    if category:
        params['categories'] = category
    if alcohol and alcohol.lower() == 'true':
        params['q'] = 'beer OR wine OR cocktail OR brewery'

    headers = {
        'Authorization': f'Bearer {settings.EVENTBRITE_TOKEN}'
    }

    try:
        r = requests.get(EVENTBRITE_SEARCH_URL, headers=headers, params=params, timeout=10)
        
        # Check if the request was successful
        if r.status_code == 200:
            data = r.json()
            events = data.get('events', [])
            return Response({'events': events})
        else:
            # API returned an error, use mock data
            raise requests.HTTPError(f"Eventbrite API returned {r.status_code}")
            
    except (requests.HTTPError, requests.RequestException) as e:
        # Return mock data when Eventbrite API fails
        mock_events = [
            {
                "id": "mock_1",
                "name": {"text": "Tech Meetup London"},
                "logo": {"url": "https://via.placeholder.com/150x150/FF6B6B/FFFFFF?text=Tech"},
                "description": {"text": "A great tech meetup in London"},
                "url": "https://example.com/event1"
            },
            {
                "id": "mock_2", 
                "name": {"text": "Art Gallery Opening"},
                "logo": {"url": "https://via.placeholder.com/150x150/4ECDC4/FFFFFF?text=Art"},
                "description": {"text": "Contemporary art showcase"},
                "url": "https://example.com/event2"
            },
            {
                "id": "mock_3",
                "name": {"text": "Food Festival Weekend"},
                "logo": {"url": "https://via.placeholder.com/150x150/45B7D1/FFFFFF?text=Food"},
                "description": {"text": "Local food vendors and live music"},
                "url": "https://example.com/event3"
            },
            {
                "id": "mock_4",
                "name": {"text": "Live Jazz Night"},
                "logo": {"url": "https://via.placeholder.com/150x150/96CEB4/FFFFFF?text=Jazz"},
                "description": {"text": "Smooth jazz with cocktails"},
                "url": "https://example.com/event4"
            },
            {
                "id": "mock_5",
                "name": {"text": "Comedy Show Tonight"},
                "logo": {"url": "https://via.placeholder.com/150x150/FFD93D/FFFFFF?text=Comedy"},
                "description": {"text": "Stand-up comedy with local comedians"},
                "url": "https://example.com/event5"
            }
        ]
        # Return random selection of mock events
        selected_events = random.sample(mock_events, min(3, len(mock_events)))
        return Response({
            'events': selected_events,
            'using_mock_data': True,
            'note': 'Using demo data - Eventbrite API unavailable',
            'filters_applied': {
                'location': location,
                'price': price,
                'alcohol': alcohol,
                'category': category
            }
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
