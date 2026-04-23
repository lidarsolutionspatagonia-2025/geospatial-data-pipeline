import geopandas as gpd
import os

INPUT_PATH = "../data/raw/provincia.shp"
OUTPUT_PATH = "../data/processed/provincia.geojson"

def main():
    print("Loading shapefile...")
    gdf = gpd.read_file(INPUT_PATH)

    print("CRS:", gdf.crs)

    gdf = gdf.to_crs(epsg=4326)

    print("Processing geometries...")
    gdf["area_km2"] = gdf.geometry.area / 10**6

    print("Saving GeoJSON...")
    os.makedirs("../data/processed", exist_ok=True)
    gdf.to_file(OUTPUT_PATH, driver="GeoJSON")

    print("Done. Output:", OUTPUT_PATH)

if __name__ == "__main__":
    main()