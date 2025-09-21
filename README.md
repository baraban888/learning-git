# Projekt: Filmoteka 🎬

Projekt edukacyjny w Pythonie, pokazujący wykorzystanie **programowania obiektowego**.  
Celem zadania było stworzenie systemu zarządzania biblioteką filmów i seriali.  

---

## Funkcjonalność

1. **Klasy**:
   - `Movie` – reprezentuje film (tytuł, rok, gatunek, liczba odtworzeń).
   - `Series` – reprezentuje odcinek serialu (tytuł, rok, gatunek, sezon, odcinek, liczba odtworzeń).
   - Obie klasy dziedziczą po klasie bazowej `Video`.

2. **Metoda `play()`**  
   - Zwiększa liczbę odtworzeń danego filmu lub odcinka o `1`.

3. **Format wyświetlania**  
   - Film: `Tytuł (Rok)`  
   - Serial: `Tytuł S01E05`

4. **Biblioteka**  
   - Wszystkie filmy i seriale przechowywane są w jednej liście `library`.

5. **Funkcje pomocnicze**  
   - `get_movies()` – zwraca listę filmów.  
   - `get_series()` – zwraca listę seriali.  
   - `search(title)` – wyszukuje film/serial po tytule.  
   - `generate_views()` – losowo wybiera element i dodaje mu odtworzenia (1–100).  
   - `generate_views_x10()` – powtarza `generate_views` 10 razy.  
   - `top_titles(n)` – zwraca najpopularniejsze tytuły według liczby odtworzeń.  

---

## Jak uruchomić

1. Sklonuj repozytorium i przejdź do gałęzi `filmoteka`:
   bash
   git checkout filmoteka
