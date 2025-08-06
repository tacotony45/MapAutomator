import requests

def fetch_osm_data(bbox):
    """
    Fetches highway data from OpenStreetMap using Overpass API within the bbox.

    bbox format: "south,west,north,east"
    """
    url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      way["highway"]({bbox});
    );
    out geom;
    """
    try:
        response = requests.post(url, data={'data': query}, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Overpass API: {e}")
        return None
