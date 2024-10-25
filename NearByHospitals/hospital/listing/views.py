from django.shortcuts import render
import requests

# Function to fetch hospitals from OpenStreetMap API
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
        return response.json()  # This returns a dictionary
    else:
        return None

# Function to get latitude and longitude from pincode using Nominatim API
def get_lat_lon_from_pincode(pincode):
    nominatim_url = f"https://nominatim.openstreetmap.org/search?postalcode={pincode}&format=json&addressdetails=1"
    response = requests.get(nominatim_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return (data[0]['lat'], data[0]['lon'])
    
    return None

# Django view to handle form submission and show results
def hospital_list(request):
    hospitals_data = []
    
    if request.method == 'POST':
        pincode = request.POST.get('pincode')  # Get the pincode from the form
        
        # Get latitude and longitude from pincode
        location = get_lat_lon_from_pincode(pincode)
        
        if location:
            lat, lon = location
            # Fetch hospital data
            hospitals = fetch_hospitals(lat, lon)
            
            if hospitals:
                # Extract relevant data for each hospital
                for hospital in hospitals['elements']:
                    if 'tags' in hospital:
                        name = hospital['tags'].get('name', 'N/A')
                        lat = hospital.get('lat', 'N/A')
                        lon = hospital.get('lon', 'N/A')
                        address = hospital['tags'].get('addr:full', 'N/A')
                        hospitals_data.append({
                            'name': name,
                            'lat': lat,
                            'lon': lon,
                            'address': address
                        })
    
    # Render the template with hospitals data
    return render(request, 'listing/hospital_list.html', {'hospitals': hospitals_data})

