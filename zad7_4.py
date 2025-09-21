import random

# --- Klasa bazowa ---
class Video:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        """Zwiększa liczbę odtworzeń o 1"""
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.year})"


# --- Klasa Film ---
class Movie(Video):
    pass  # dziedziczy wszystko z Video


# --- Klasa Serial ---
class Series(Video):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"


# --- Lista biblioteki ---
library = []


# --- Funkcje pomocnicze ---
def get_movies():
    """Zwraca tylko filmy"""
    return [item for item in library if isinstance(item, Movie)]


def get_series():
    """Zwraca tylko seriale"""
    return [item for item in library if isinstance(item, Series)]


def search(title):
    """Szukaj filmu/serialu po tytule"""
    for item in library:
        if item.title.lower() == title.lower():
            return item
    return None


def generate_views():
    """Losowo wybiera film/serial i dodaje mu 1–100 odtworzeń"""
    item = random.choice(library)
    item.views += random.randint(1, 100)


def generate_views_x10():
    """Powtarza generate_views 10 razy"""
    for _ in range(10):
        generate_views()


def top_titles(n=3):
    """Zwraca n najpopularniejszych pozycji"""
    return sorted(library, key=lambda x: x.views, reverse=True)[:n]


# --- Test ---
if __name__ == "__main__":
    # Dodajemy filmy
    library.append(Movie("Pulp Fiction", 1994, "Crime"))
    library.append(Movie("Matrix", 1999, "Sci-Fi"))

    # Dodajemy serial
    library.append(Series("Simpsons", 1989, "Comedy", 1, 5))
    library.append(Series("Simpsons", 1989, "Comedy", 1, 6))

    # Generujemy widoki
    generate_views_x10()

    # Wyświetlamy top 3
    print("\nTop titles:")
    for item in top_titles(3):
        print(f"{item} — {item.views} odtworzeń")
