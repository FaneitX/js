from typing import List
from ..models.meal import Meal

def filter_meals_by_type(meals: List[Meal], meal_type: str) -> List[Meal]:
    """Filtruje posiłki według typu używając programowania funkcyjnego"""
    return list(filter(lambda m: m.meal_type == meal_type, meals))

def get_prep_times(meals: List[Meal]) -> List[int]:
    """Pobiera czasy przygotowania używając map"""
    return list(map(lambda m: m.prep_time, meals))