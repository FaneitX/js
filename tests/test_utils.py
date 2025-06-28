import unittest
import os
import json
from tempfile import NamedTemporaryFile
from meal_planner.utils.file_operations import save_to_json, load_from_json
from meal_planner.utils.filters import filter_meals_by_type, get_prep_times
from meal_planner.models.meal import Meal

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_data = {'key': 'value'}
        self.temp_file = NamedTemporaryFile(delete=False, suffix='.json')
        
    def tearDown(self):
        os.unlink(self.temp_file.name)
        
    def test_save_and_load_json(self):
        save_to_json(self.test_data, self.temp_file.name)
        loaded_data = load_from_json(self.temp_file.name)
        self.assertEqual(self.test_data, loaded_data)

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.meals = [
            Meal("Oatmeal", "breakfast", ["oats"], 10),
            Meal("Salad", "lunch", ["lettuce"], 15),
            Meal("Soup", "lunch", ["vegetables"], 20)
        ]
        
    def test_filter_meals_by_type(self):
        lunches = filter_meals_by_type(self.meals, "lunch")
        self.assertEqual(len(lunches), 2)
        self.assertTrue(all(m.meal_type == "lunch" for m in lunches))
        
    def test_get_prep_times(self):
        times = get_prep_times(self.meals)
        self.assertEqual(times, [10, 15, 20])

if __name__ == '__main__':
    unittest.main()