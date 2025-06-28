class FileOperationError(Exception):
    """Własny wyjątek dla operacji na plikach"""
    pass

class MealValidationError(Exception):
    """Własny wyjątek dla walidacji posiłków"""
    pass

class PlanOperationError(Exception):
    """Własny wyjątek dla operacji na planach"""
    pass