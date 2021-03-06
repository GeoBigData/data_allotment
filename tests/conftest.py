from shapely.geometry import shape
import pandas as pd
import pytest
import json
import os


@pytest.fixture(scope='session')
def data_dir():
    """Absolute file path to the directory containing test datasets."""
    return os.path.abspath(os.path.join('data'))


@pytest.fixture(scope='session')
def path_gb100_to_km2(data_dir):
    return os.path.join(data_dir, '100gb_to_km2.csv')


@pytest.fixture(scope='session')
def path_km100_to_gb(data_dir):
    return os.path.join(data_dir, 'km100_to_gb.csv')


@pytest.fixture(scope='session')
def gbdxsearch_results(data_dir):
    path = os.path.join(data_dir, 'gbdxsearch_results.json')
    with open(path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def gbdxsearch_resultsdf(data_dir):
    path = os.path.join(data_dir, 'gbdxsearch_formatted.csv')
    return pd.read_csv(path)


@pytest.fixture(scope='session')
def search_intersection_geom(data_dir):
    path = os.path.join(data_dir, 'search_intersection.geojson')
    with open(path, 'r') as f:
        geojson = json.load(f)
    return shape(geojson['geometry'])
