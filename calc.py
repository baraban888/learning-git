import logging

# konfiguracja logowania
logging.basicConfig(level=logging.INFO, format="%(message)s")

print("Wybierz działanie: 1 - Dodawanie, 2 - Odejmowanie")
choice = input("Twój wybór: ")

# Funkcja pomocnicza: pyta o liczbę dopóki użytkownik nie poda poprawnej
def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            logging.error(f"'{value}' to nie jest liczba! Spróbuj ponownie.")

a = get_number("Podaj składnik 1: ")
b = get_number("Podaj składnik 2: ")

if choice == "1":
    result = a + b
    logging.info(f"Dodaję {a} + {b}")
elif choice == "2":
    result = a - b
    logging.info(f"Odejmuję {a} - {b}")
else:
    logging.error("Niepoprawny wybór działania!")
    result = None

if result is not None:
    print("Wynik to:", result)
