from api_client import fetch_osm_data
from exporter import save_osm_to_file

bbox = "36.12,-115.20,36.18,-115.10"  # Las Vegas area
print("Fetching data...")
data = fetch_osm_data(bbox)

if data is None:
    print("Failed to fetch data.")
else:
    print(f"Fetched {len(data['elements'])} elements")
    print("Saving to GeoJSON...")
    save_osm_to_file(data, "las_vegas_highways.geojson")
    print("Done.")
