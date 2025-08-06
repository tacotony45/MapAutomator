import geopandas as gpd
from shapely.geometry import LineString

def save_osm_to_file(osm_data, output_file="output.geojson"):
    """
    Converts OSM highway data to GeoJSON or Shapefile and saves it.
    """
    features = []
    for element in osm_data['elements']:
        if element['type'] == 'way' and 'geometry' in element:
            coords = [(pt['lon'], pt['lat']) for pt in element['geometry']]
            if len(coords) > 1:
                features.append({
                    "geometry": LineString(coords),
                    "properties": element['tags'] if 'tags' in element else {}
                })
    
    if not features:
        print("No features to save.")
        return

    gdf = gpd.GeoDataFrame(
        [f["properties"] for f in features],
        geometry=[f["geometry"] for f in features],
        crs="EPSG:4326"
    )
    gdf.to_file(output_file, driver="GeoJSON" if output_file.endswith(".geojson") else "ESRI Shapefile")
    print(f"Data saved to {output_file}")
