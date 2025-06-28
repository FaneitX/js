import json
from pathlib import Path
from typing import Union, Dict, List
from ..models.meal import Meal
from ..models.plan import Plan
from ..exceptions import FileOperationError

def save_to_json(data: Union[Dict, List], file_path: Union[str, Path]) -> None:
    """Zapisuje dane do pliku JSON z obsługą błędów"""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except (IOError, TypeError) as e:
        raise FileOperationError(f"Błąd zapisu do {file_path}: {str(e)}")

def load_from_json(file_path: Union[str, Path]) -> Union[Dict, List]:
    """Wczytuje dane z pliku JSON z obsługą błędów"""
    try:
        with open(file_path) as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        raise FileOperationError(f"Błąd wczytywania z {file_path}: {str(e)}")

def save_plan(plan: Plan, file_path: Union[str, Path]) -> None:
    """Zapisuje plan posiłków do pliku"""
    save_to_json(plan.to_dict(), file_path)

def load_plan(file_path: Union[str, Path]) -> Plan:
    """Wczytuje plan posiłków z pliku"""
    data = load_from_json(file_path)
    return Plan.from_dict(data)