import requests
from django.shortcuts import render

def fetch_hospitals(lat, lon, radius=5000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:{radius},{lat},{lon});
      way["amenity"="hospital"](around:{radius},{lat},{lon});
      relation["amenity"="hospital"](around:{radius},{lat},{lon});
    );
    out body;
    """
    
    response = requests.post(overpass_url, data={'data': overpass_query})
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_lat_lon_from_pincode(pincode):
    # Use Nominatim API to convert pincode to latitude and longitude
    nominatim_url = f"https://nominatim.openstreetmap.org/search?postalcode={pincode}&format=json&addressdetails=1"
    
    try:
        response = requests.get(nominatim_url)
        if response.status_code == 200:
            data = response.json()
            if data:
                # Return the latitude and longitude of the first result
                return (data[0]['lat'], data[0]['lon'])
    except Exception as e:
        print(f"Error fetching lat/lon for pincode {pincode}: {e}")
    
    return None  # Return None if no data is found

def hospital_list(request):
    hospitals = []
    if request.method == 'GET':
        pincode = request.GET.get('pincode')
        
        # Get latitude and longitude from pincode
        lat_lon = get_lat_lon_from_pincode(pincode)
        if lat_lon:
            lat, lon = lat_lon
            data = fetch_hospitals(lat, lon)
            if data:
                hospitals = data.get('elements', [])
        else:
            # Handle the case where lat/lon could not be fetched
            hospitals = []  # No hospitals found or unable to fetch lat/lon

    return render(request, 'listing/hospital_list.html', {'hospitals': hospitals})
