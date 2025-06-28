import unittest
from meal_planner.models.meal import Meal
from meal_planner.models.plan import Plan

class TestMeal(unittest.TestCase):
    def test_meal_creation(self):
        meal = Meal("Test", "obiad", ["składnik1", "składnik2"], 30)
        self.assertEqual(meal.name, "Test")
        self.assertEqual(meal.meal_type, "obiad")
        
    def test_serialization(self):
        meal = Meal("Test", "obiad", ["składnik1", "składnik2"], 30)
        meal_dict = meal.to_dict()
        new_meal = Meal.from_dict(meal_dict)
        self.assertEqual(meal.name, new_meal.name)

class TestPlan(unittest.TestCase):
    def setUp(self):
        self.plan = Plan(1)
        self.meal = Meal("Test", "obiad", ["składnik1", "składnik2"], 30)
        
    def test_add_meal(self):
        self.plan.add_meal("Poniedziałek", "obiad", self.meal)
        self.assertEqual(self.plan.days["Poniedziałek"]["obiad"], self.meal)
        
    def test_filter_meals(self):
        self.plan.add_meal("Poniedziałek", "obiad", self.meal)
        lunches = self.plan.get_meals_by_type("obiad")
        self.assertEqual(len(lunches), 1)
        self.assertEqual(lunches[0], self.meal)

if __name__ == "__main__":
    unittest.main()