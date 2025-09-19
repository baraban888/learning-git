# Projekt: Wizytówki

Projekt edukacyjny w Pythonie, pokazujący pracę z klasami, metodami oraz dziedziczeniem.  
Do generowania losowych danych wykorzystano bibliotekę [Faker](https://faker.readthedocs.io).

## Funkcjonalność

- Klasa `BaseContact`: przechowuje podstawowe dane (imię, nazwisko, telefon prywatny, e-mail).
- Klasa `BusinessContact`: dziedziczy po `BaseContact`, rozszerza dane o:
  - stanowisko,
  - nazwę firmy,
  - telefon służbowy.
- Metoda `contact()`: wyświetla komunikat z wyborem numeru telefonu i danymi kontaktu.
- Właściwość `label_length`: zwraca długość imienia i nazwiska (przydatne np. do adresowania).
- Funkcja `create_contacts(contact_type, quantity)`: tworzy listę wizytówek wybranego typu i w zadanej ilości.

## Instalacja

Utwórz i aktywuj środowisko wirtualne, a następnie zainstaluj zależności:
bash
pip install -r requirements.txt

## Użycie

Uruchom plik:
python zad1_book.py

Przykładowy wynik
Jan Kowalski - [jan.kowalski@example.com]
Wybieram numer +48 123456789 i dzwonię do Jan Kowalski
label_length = 11

Wymagania

Python 3.10+
Faker (patrz requirements.txt)

Autor: Alex
Zadanie w ramach bootcampu (moduł: Metody w klasach, dziedziczenie).
