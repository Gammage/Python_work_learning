from city_functions import city_country

def test_city_country():
    """tests the city and country variable"""
    test_format_city_country = city_country('london','england')
    assert test_format_city_country == 'london england'