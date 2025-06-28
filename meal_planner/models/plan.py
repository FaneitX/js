from typing import List, Dict
from .meal import Meal

class Plan:
    """Kontener dla tygodniowych planów posiłków"""
    
    def __init__(self, week_number: int):
        self.week_number = week_number
        self.days = {
            'Poniedziałek': {'śniadanie': None, 'obiad': None, 'kolacja': None},
            'Wtorek': {'śniadanie': None, 'obiad': None, 'kolacja': None},
            # ... inne dni
        }
        
    def add_meal(self, day: str, meal_type: str, meal: Meal):
        """Dodaje posiłek do planu"""
        if day not in self.days:
            raise ValueError(f"Nieprawidłowy dzień: {day}")
        if meal_type not in self.days[day]:
            raise ValueError(f"Nieprawidłowy typ posiłku: {meal_type}")
            
        self.days[day][meal_type] = meal
        
    def get_meals_by_type(self, meal_type: str) -> List[Meal]:
        """Pobiera wszystkie posiłki określonego typu"""
        return [day[meal_type] for day in self.days.values() if day[meal_type] is not None]
        
    def to_dict(self):
        """Konwertuje plan na słownik do serializacji"""
        return {
            'week_number': self.week_number,
            'days': {
                day: {
                    mtype: meal.to_dict() if meal else None
                    for mtype, meal in day_meals.items()
                }
                for day, day_meals in self.days.items()
            }
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Tworzy Plan ze słownika"""
        plan = cls(data['week_number'])
        for day, day_meals in data['days'].items():
            for mtype, meal_data in day_meals.items():
                if meal_data:
                    plan.add_meal(day, mtype, Meal.from_dict(meal_data))
        return plan