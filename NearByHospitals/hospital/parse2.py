import json
import requests

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
        print("Fetched hospitals successfully.")
        return response.json()  # This returns a dictionary
    else:
        print(f"Failed to fetch hospitals: {response.status_code}, {response.text}")
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

if __name__ == '__main__':
    pincode = 208012
    print(f"Fetching lat/lon for pincode {pincode}...")
    l = get_lat_lon_from_pincode(pincode)
    
    if l:
        lat, lon = l
        print(f"Latitude: {lat}, Longitude: {lon}")
        data = fetch_hospitals(lat, lon)

        if data:  # Ensure data is not None before proceeding
            hospitals = data['elements']
            print(f"Found {len(hospitals)} hospitals.")
            for hospital in hospitals:
                if 'tags' in hospital:
                    name = hospital['tags'].get('name', 'N/A')
                    lat = hospital.get('lat', 'N/A')
                    lon = hospital.get('lon', 'N/A')
                    address = hospital['tags'].get('addr:full', 'N/A')
                    print(f"Hospital Name: {name}, Latitude: {lat}, Longitude: {lon}, Address: {address}")
        else:
            print("No hospital data retrieved.")
    else:
        print("Could not get latitude and longitude from the pincode.")

