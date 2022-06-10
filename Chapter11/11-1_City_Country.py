# May 24.2022

def city_country(city, country):
    """Returns a neatly formated line containing a city and country."""
    city_country = f"{city.title()}, {country.title()}"
    return city_country

my_city = city_country('edmonton', 'canada')
print(my_city)
