# May 18.2022

def city_country(city='', country=''):
    """Returns capitalized city, country."""
    city = input("City: ")
    country = input ("Country: ")
    city_country = f"{city}, {country}"
    return city_country.title()

answer = city_country()
print(answer)
