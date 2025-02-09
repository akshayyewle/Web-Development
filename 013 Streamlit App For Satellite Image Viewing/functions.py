from st_files_connection import FilesConnection
from pystac_client import Client
from odc.stac import load

def search_satellite_images(collection="sentinel-2-l2a",
                            bbox=[-120.15,38.93,-119.88,39.25],
                            date="2023-06-01/2023-06-30",
                            cloud_cover=(0, 10)):

    # Define the search client
    client=Client.open("https://earth-search.aws.element84.com/v1")
    search = client.search(collections=[collection],
                            bbox=bbox,
                            datetime=date,
                            query=[f"eo:cloud_cover<{cloud_cover[1]}", f"eo:cloud_cover>{cloud_cover[0]}"])

    # Print the number of matched items
    print(f"Number of images found: {search.matched()}")

    data = load(search.items(), bbox=bbox, groupby="solar_day", chunks={})

    print(f"Number of days in data: {len(data.time)}")

    return data

def get_bbox_with_buffer(latitude=37.2502, longitude=-119.7513, buffer=0.01):

    min_lat = latitude - buffer
    max_lat = latitude + buffer
    min_lon = longitude - buffer
    max_lon = longitude + buffer

    bbox = [min_lon, min_lat, max_lon, max_lat]
    return bbox

# Image Visualization
def count_classified_pixels(data,num):

    scl_image = data[["scl"]].isel(time=num).to_array()

    # Count the classified pixels 
    count_saturated = np.count_nonzero(scl_image == 1)        # Saturated or defective
    count_dark = np.count_nonzero(scl_image == 2)             # Dark Area Pixels
    count_cloud_shadow = np.count_nonzero(scl_image == 3)     # Cloud Shadows
    count_vegetation = np.count_nonzero(scl_image == 4)       # Vegetation
    count_soil = np.count_nonzero(scl_image == 5)             # Bare Soils
    count_water = np.count_nonzero(scl_image == 6)            # Water
    count_clouds_low= np.count_nonzero(scl_image == 7)        # Clouds Low Probability / Unclassified
    count_clouds_med = np.count_nonzero(scl_image == 8)       # Clouds Medium Probability
    count_clouds_high = np.count_nonzero(scl_image == 9)      # Clouds High Probability
    count_clouds_cirrus = np.count_nonzero(scl_image == 10)   # Cirrus
    count_clouds_snow = np.count_nonzero(scl_image == 11)     # Snow

    counts = {
    'Dark/Bright': count_cloud_shadow +count_dark+count_clouds_low+count_clouds_med+count_clouds_high+count_clouds_cirrus +count_clouds_snow +count_saturated,
    'Vegetation': count_vegetation,
    'Bare Soil': count_soil,
    'Water': count_water,
    }

    return counts