# May 24.2022

def city_country(city, country, population=''):
    """Returns a neatly formated line containing a city and country."""
    city_country = f"{city.title()}, {country.title()}"
    if population:
        city_country += f" - population {population}"
    return city_country

my_city = city_country('edmonton', 'canada', '1,000,000')
print(my_city)
