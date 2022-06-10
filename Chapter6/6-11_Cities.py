# May 14.2022

cities = {
    'edmonton': {
        'country': 'canada',
        'population': 1100000,
        'fact': 'stinky',
        },
    'islamabad': {
        'country': 'pakistan',
        'population': 1000000,
        'fact': 'islamic',
        },
    'st. petersburg': {
        'country': 'russia',
        'population': 5000000,
        'fact': 'hella cool',
        },
    }

##for city, dictionary in cities.items():
##    for category, info in dictionary.items():
##        country = info['country'].title()
##        population = info['population']
##        fact = info['fact']
##        print(f"\n{city.title()}:")
##        print(f"  - {country}")
##        print(f"  - {population}")
##        print(f"  - {fact}")


for city, city_info in cities.items():
    print(f"\nHere is some information about {city.title()}:")
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print(f"  - Country: {country}")
    print(f"  - Population: {population}")
    print(f"  - Fact: {fact}")
