import unittest

import sys
import pathlib
# parent.parent.parent - three levels up
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from functions import car_search, get_workers_list

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

car_data_empty = {}

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]


class MyTestAboutDict(unittest.TestCase):

    """
    Test 1 - Positive
    Valid search criteria should return not empty list
    """
    def test_1_search(self):
        print('\n ++++++ Test 1 +++++++')
        search_criteria = (2017, 1.6, 36000)
        price_list = []
        if len(car_data) != 0:
            car_search_result = car_search(car_data=car_data, search_criteria=search_criteria, search_length=5)
            self.assertTrue(len(car_search_result) != 0, "Search result is empty")
            # Check that result list was sorted properly
            for name, description in car_search_result:
                price_list.append(description[4])
                print(price_list)
            i = 0
            self.assertFalse(price_list[i+1] <= price_list[i], "Prices were filtered incorrect")
        else:
            self.assertTrue("Search criteria or car_data is empty, search cannot be done")

    """
    Test 2 - Invalid year in search
    Result should return empty list
    """

    def test_2_search(self):
        print('\n ++++++ Test 2 +++++++')
        search_criteria = (2027, 1.6, 36000)
        if len(car_data) != 0:
            car_search_result = car_search(car_data=car_data, search_criteria=search_criteria, search_length=5)
            self.assertTrue(len(car_search_result) == 0, "Test 2 failed, Empty list for this search expected")
        else:
            self.assertTrue("The car_data is empty, search cannot be done")

    """
    Test 3 - Empty car data
    Test failure is expected
    """

    def test_3_search(self):
        print('\n ++++++ Test 3 +++++++')
        search_criteria = (0, 0, 0)
        if len(car_data) != 0:
            car_search_result = car_search(car_data=car_data, search_criteria=search_criteria, search_length=0)
            print(car_search_result)
            self.assertEqual(len(car_search_result), 0, "Test 3 failed, No result for car search is expected")
        else:
            self.assertTrue("The car_data is empty, search cannot be done")

    """
    Test 4 - Positive
    Check that filtered result is not empty
    """

    def test_4_workers(self):
        print('\n ++++++ Test 4 +++++++')
        param = 30
        assert len(people_records) != 0, "List of workers are empty, no search is possible"
        result = get_workers_list(people_records, param)
        assert len(result) != 0, "List of workers is empty"

    """
    Test 5 - Negative
    Check that filtered result is empty for invalid param
    """

    def test_5_workers(self):
        print('\n ++++++ Test 5 +++++++')
        param = 100
        assert len(people_records) != 0, "List of workers are empty, no search is possible"
        result = get_workers_list(people_records, param)
        assert len(result) == 0, "Expected List of workers should be empty"


if __name__ ==('__main__'):
    unittest.main()
