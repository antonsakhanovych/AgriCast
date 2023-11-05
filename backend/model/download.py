# !/usr/bin/env python
import cdsapi
import pygrib

c = cdsapi.Client()

c.retrieve(
    'sis-agroclimatic-indicators',
    {
        'format': 'zip',
        'origin': 'hadgem2_es_model',
        'experiment': 'rcp4_5',
        'temporal_aggregation': 'season',
        'period': '201101_204012',
        'variable': [
            'cold_spell_duration_index', 'maximum_number_of_consecutive_dry_days', 'maximum_number_of_consecutive_frost_days',
            'maximum_number_of_consecutive_summer_days', 'maximum_number_of_consecutive_wet_days', 'warm_and_wet_days',
            'warm_spell_duration_index',
        ],
        'version': '1.1',
    },
    'climate.zip')

def read_and_print_grib_data(file_path):
    try:
        grbs = pygrib.open(file_path)

        for grb in grbs:
            # List available keys for the GRIB record
            keys = grb.keys()
            print("Available Keys:", keys)

            # Choose a key to access the data
            chosen_key = "values"  # Change this to the desired key

            if chosen_key in keys:
                data = grb[chosen_key]
                print(f"Key: {chosen_key}")
                print(f"Data Shape: {data.shape}")
                print(f"Data: {data}")
                print("\n")
            else:
                print(f"Key '{chosen_key}' not found in the GRIB record.")

    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     # Example usage:
#     file_path = "download.grib"
#     read_and_print_grib_data(file_path)
