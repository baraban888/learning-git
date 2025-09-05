# Kalkulator (`calc.py`)

Prosty kalkulator w Pythonie obsługujący dodawanie i odejmowanie dwóch liczb. Wejście jest walidowane — program prosi o ponowne podanie liczby, jeśli użytkownik wpisze niepoprawną wartość. Dziennik zdarzeń (logi) jest wypisywany za pomocą biblioteki `logging`.

## Wymagania

- Python 3.8+
- Brak dodatkowych bibliotek

## Uruchomienie

```bash
python calc.py
```

## Jak działa

1. Program pyta o działanie:  
    `1` - Dodawanie  
    `2` - Odejmowanie
2. Prosi o dwie liczby (wielokrotnie, aż podasz poprawne).
3. Wykonuje obliczenie i drukuje wynik.
4. Informacje o przebiegu działania są wypisywane przez `logging`.

### Przykład

```
Wybierz działanie: 1 - Dodawanie, 2 - Odejmowanie
Twój wybór: 1
Podaj składnik 1: 2.3
Podaj składnik 2: 5.4
Dodaję 2.3 + 5.4
Wynik to: 7.7
```

## Struktura kodu (skrót)

Konfiguracja logowania:
```python
logging.basicConfig(level=logging.INFO, format="%(message)s")
```

Walidacja wejścia (pętla do skutku):
```python
def get_number(prompt):
     while True:
          value = input(prompt)
          try:
                return float(value)
          except ValueError:
                logging.error(f"'{value}' to nie jest liczba! Spróbuj ponownie.")
```

### Zmiana poziomu logów

Jeśli chcesz widzieć więcej komunikatów (np. DEBUG), zmień poziom:
```python
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
```

## Znane ograniczenia

- Obsługuje tylko dodawanie i odejmowanie dwóch liczb.
- Brak obsługi liczb bardzo dużych/niestandardowych formatów.

## Licencja

Projekt edukacyjny — do użytku własnego w ramach nauki.