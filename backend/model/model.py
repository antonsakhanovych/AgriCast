import matplotlib.pyplot as plt
import cdsapi
import pandas as pd
import numpy as np


def download_climate_data():
    c = cdsapi.Client()

    c.retrieve(
        'sis-agroclimatic-indicators',
        {
            'format': 'zip',
            'variable': 'biologically_effective_degree_days',
            'experiment': 'rcp4_5',
            'origin': 'gfdl_esm2m_model',
            'temporal_aggregation': '10_day',
            'period': '201101_204012',
            'version': '1.1',
        },
        'climate.zip')

def download_crops_data():
    c = cdsapi.Client()
    c.retrieve(
        'sis-agroproductivity-indicators',
        {
            'format': 'zip',
            'product_family': 'crop_productivity_indicators',
            'variable': [
                'crop_development_stage', 'total_above_ground_production', 'total_weight_storage_organs',
            ],
            'crop_type': 'spring_wheat',
            'year': '2012',
            'month': [
                '03', '04', '05',
            ],
            'day': [
                '10', '20', '30',
                '31',
            ],
            'growing_season': '1st_season_per_campaign',
            'harvest_year': '2012',
        },
        'crops.zip')

def split_train_test(data, test_ratio):
    shuffled_indexes = np.random.permutation(len(data))
    test_set_size = len(data) * test_ratio
    train_indexes = shuffled_indexes[test_set_size:]
    test_indexes = shuffled_indexes[:test_set_size]
    return data.iloc[train_indexes], data.iloc[test_indexes]

if __name__ == "__main__":
    download_climate_data()
    # download_crops_data()

