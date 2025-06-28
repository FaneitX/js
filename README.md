# Tygodniowy Planer Posiłków

Aplikacja w Pythonie do tworzenia i zarządzania tygodniowymi planami posiłków.

## Funkcje
- Tworzenie i zarządzanie posiłkami ze składnikami i czasem przygotowania
- Budowanie tygodniowych planów posiłków
- Filtrowanie posiłków według typu (śniadanie, obiad, kolacja)
- Zapis i wczytywanie planów do/z plików JSON
- Obsługa wyjątków dla nieprawidłowych operacji

## Instalacja
1. Sklonuj repozytorium
2. Zainstaluj wymagania: `pip install -r requirements.txt`

## Użycie
```python
from meal_planner.main import main
main()
```

## Przykładowe dane
Przykładowy posiłek:
```json
{
    "name": "Owsianka",
    "type": "śniadanie",
    "ingredients": ["płatki owsiane", "mleko", "jagody"],
    "prep_time": 10
}
```

## Autorzy
- [Twoje imię]

## Licencja
MIT
