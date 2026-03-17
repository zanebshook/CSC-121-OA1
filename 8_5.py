def describe_city(city_name, country_name='england'):
    """give information about cities"""
    print(f"{city_name.title()} is a great city to visit in {country_name.title()}")

describe_city('london')
describe_city('birmingham')
describe_city('pairs', 'france')   