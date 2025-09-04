import unicodedata
import re

def is_palindrome(text: str) -> bool:
    """
    Funkcja sprawdza, czy dany tekst jest palindromem.
    
    Argumenty:
        text (str): słowo lub tekst do sprawdzenia.
    
    Zwraca:
        bool: True jeśli tekst jest palindromem, False jeśli nie.
    """
    # 1. Zamieniamy wszystkie litery na małe (np. "Kajak" -> "kajak")
    normalized_text = text.lower()
    
    # 2. Usunięcie znaków diakrytycznych (ą -> a, ł -> l, ż -> z itp.)
    normalized_text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    
    # 3. Usunięcie wszystkiego, co nie jest literą ani cyfrą
    #    (spacje, przecinki, kropki itd.)
    normalized_text = re.sub(r'[^a-z0-9]', '', text)

    # 4. Sprawdzamy, czy tekst jest równy swojemu odbiciu (rewersowi)
    return normalized_text == normalized_text[::-1]


# Przykłady użycia
print(is_palindrome("kajak"))   # True
print(is_palindrome("potop"))   # True
print(is_palindrome("kot"))     # False
print(is_palindrome("KayaK"))   # True (niezależnie od wielkości liter)
print(is_palindrome("morze"))   # False
