# May 24.2022

import unittest
from City_Country import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'City_Country.py'."""

    def test_city_country(self):
        """Does 'Edmonton, Canada' work?"""
        formatted_city_country = city_country('edmonton', 'canada')
        self.assertEqual(formatted_city_country, 'Edmonton, Canada')

    def test_city_country_population(self):
        """Does 'Santiago, Chile - population 5,000,000' work?"""
        formatted_city_country = city_country(
            'santiago', 'chile', '5,000,000',
            )
        self.assertEqual(
            formatted_city_country,
            'Santiago, Chile - population 5,000,000',
            )

if __name__ == '__main__':
    unittest.main()
