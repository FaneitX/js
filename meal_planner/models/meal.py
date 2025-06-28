class Meal:
    """Klasa reprezentująca pojedynczy posiłek"""
    
    def __init__(self, name: str, meal_type: str, ingredients: list, prep_time: int):
        self.name = name
        self.meal_type = meal_type  # śniadanie, obiad, kolacja, przekąska
        self.ingredients = ingredients
        self.prep_time = prep_time  # w minutach
        
    def __str__(self):
        return f"{self.name} ({self.meal_type})"
        
    def to_dict(self):
        """Konwertuje posiłek na słownik do serializacji"""
        return {
            'name': self.name,
            'type': self.meal_type,
            'ingredients': self.ingredients,
            'prep_time': self.prep_time
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Tworzy Meal ze słownika"""
        return cls(
            name=data['name'],
            meal_type=data['type'],
            ingredients=data['ingredients'],
            prep_time=data['prep_time']
        )