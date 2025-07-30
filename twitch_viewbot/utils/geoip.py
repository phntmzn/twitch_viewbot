import random

GEO_LOCATIONS = [
    {"country": "US", "city": "New York", "lat": 40.7128, "lon": -74.0060},
    {"country": "GB", "city": "London", "lat": 51.5074, "lon": -0.1278},
    {"country": "DE", "city": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"country": "JP", "city": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"country": "BR", "city": "São Paulo", "lat": -23.5505, "lon": -46.6333},
    {"country": "IN", "city": "Mumbai", "lat": 19.0760, "lon": 72.8777}
]

def get_random_location():
    return random.choice(GEO_LOCATIONS)
