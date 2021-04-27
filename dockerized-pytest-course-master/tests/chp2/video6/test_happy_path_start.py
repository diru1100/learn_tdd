import pytest

from scripts import data_processor


def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    # helper function imported from conftest.py to import file data with our csv reader
    data = process_data
    header_fields = list(data[0].keys())
    assert header_fields == [
        'Country',
        'City',
        'State_Or_Province',
        'Lat',
        'Long',
        'Altitude'
    ]


def test_csv_reader_data_contents(process_data):
    """
    Happy Path Test to examine that each row
    has the appropriate data type per field
    """
    data = process_data

    for row in data:
        assert type(row['Country']) == str
        assert type(row['City']) == str
        assert type(row['State_Or_Province']) == str
        assert type(row['Lat']) == float
        assert type(row['Long']) == float
        assert type(row['Altitude']) == float

    # Basic data checks

    assert len(data) == 180
    assert data[0]['Country'] == 'Andorra'
    assert data[179]['Country'] == 'United States'


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    yield data_processor.csv_reader(city_list_location)
