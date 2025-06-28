from .models.meal import Meal
from .models.plan import Plan
from .utils.file_operations import save_plan, load_plan
from .utils.filters import filter_meals_by_type
from .exceptions import FileOperationError, MealValidationError
import sys

def main():
    try:
        # Przykładowe użycie
        breakfast = Meal("Owsianka", "śniadanie", ["płatki owsiane", "mleko", "jagody"], 10)
        lunch = Meal("Sałatka", "obiad", ["sałata", "pomidor", "ogórek"], 15)
        
        plan = Plan(1)
        plan.add_meal("Poniedziałek", "śniadanie", breakfast)
        plan.add_meal("Poniedziałek", "obiad", lunch)
        
        # Zapis i wczytanie
        save_plan(plan, "tygodniowy_plan.json")
        loaded_plan = load_plan("tygodniowy_plan.json")
        
        # Filtrowanie
        breakfasts = filter_meals_by_type(
            [meal for day in loaded_plan.days.values() for meal in day.values() if meal],
            "śniadanie"
        )
        print(f"Śniadania: {[str(b) for b in breakfasts]}")
        
    except FileOperationError as e:
        print(f"Błąd pliku: {e}", file=sys.stderr)
    except MealValidationError as e:
        print(f"Błąd walidacji posiłku: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()