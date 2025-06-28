import unittest
import os
from meal_planner.models.meal import Meal
from meal_planner.models.plan import Plan
from meal_planner.utils.file_operations import save_plan, load_plan

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_plan.json'
        self.meal1 = Meal("Breakfast", "breakfast", ["eggs"], 10)
        self.meal2 = Meal("Lunch", "lunch", ["sandwich"], 5)
        self.plan = Plan(1)
        self.plan.add_meal("Monday", "breakfast", self.meal1)
        self.plan.add_meal("Monday", "lunch", self.meal2)
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def test_save_and_load_plan(self):
        save_plan(self.plan, self.test_file)
        loaded_plan = load_plan(self.test_file)
        
        self.assertEqual(loaded_plan.week_number, 1)
        monday_meals = loaded_plan.days["Monday"]
        self.assertEqual(monday_meals["breakfast"].name, "Breakfast")
        self.assertEqual(monday_meals["lunch"].name, "Lunch")

if __name__ == '__main__':
    unittest.main()