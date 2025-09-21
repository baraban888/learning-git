from faker import Faker
import time

fake = Faker()

# --- Dekorator do mierzenia czasu wykonania funkcji ---
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()   # zapisujemy czas początkowy
        result = func(*args, **kwargs)  # uruchamiamy funkcję
        end = time.time()     # zapisujemy czas końcowy
        print(f"\nCzas wykonania: {end - start:.4f} sek.")
        return result
    return wrapper

# --- Funkcja tworząca listę wizytówek ---
@timer
def create_business_cards(n=1000):
    cards = []
    for _ in range(n):
        card = {
            "imię": fake.first_name(),
            "nazwisko": fake.last_name(),
            "email": fake.email(),
            "telefon": fake.phone_number(),
            "firma": fake.company(),
        }
        cards.append(card)
    return cards

# --- Uruchomienie programu ---
if __name__ == "__main__":
    cards = create_business_cards()   # tworzymy 1000 wizytówek
    print(f"Utworzono {len(cards)} wizytówek")
    print(cards[0])   # pokazujemy przykład jednej wizytówki
