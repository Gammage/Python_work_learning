from city_functions import city_country

def test_city_country():
    """tests the city and country variable"""
    test_format_city_country = city_country('london','england',)
    assert test_format_city_country == 'london england'
    
def test_city_country_population():
    """tests the population parameter"""
    test_format_city_country_population = city_country('london','england','500000')
    assert test_format_city_country_population == 'london england 500000'