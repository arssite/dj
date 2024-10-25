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
        return response.json()
    else:
        return None

# Example usage
if __name__ == "__main__":
    latitude = 28.6102   # Example latitude for Delhi
    longitude = 77.2295  # Example longitude for Delhi
    radius = 5000        # Radius in meters

    hospitals = fetch_hospitals(latitude, longitude, radius)

    if hospitals:
        print("Hospitals found:")
        print(hospitals)
    else:
        print("Failed to fetch hospitals.")
