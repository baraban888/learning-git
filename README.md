📚 Domowa biblioteczka – REST API (Flask)

Projekt przedstawia proste REST API stworzone w Pythonie przy użyciu frameworka Flask.
Aplikacja umożliwia zarządzanie domową biblioteczką – dodawanie, przeglądanie, edytowanie i usuwanie książek zapisanych w pliku books.json.

🔹 Endpointy API:

Metoda	Ścieżka	Opis

GET	/api/books	Zwraca listę wszystkich książek
POST	/api/books	Dodaje nową książkę (tytuł i autor w JSON)
PUT	/api/books/<id>	Aktualizuje dane wybranej książki
DELETE	/api/books/<id>	Usuwa książkę o podanym ID

🔹 Przykład zapytania (curl):

# Dodanie książki

curl -X POST http://127.0.0.1:5000/api/books \
-H "Content-Type: application/json" \
-d "{\"title\":\"Clean Code\",\"author\":\"Robert C. Martin\"}"

🔹 Technologie:

Python 3.x

Flask

JSON

Projekt jest zgodny z zasadami PEP8, a dane są przechowywane w prostym pliku JSON bez użycia bazy danych SQL.
Kod został przetestowany lokalnie przy użyciu narzędzia curl.

### 👤 Autor

**Dmytro Bahatiuk (Alex)**  
e-mail: 1975bahat@gmail.com  
GitHub: https://github.com/<twoj-login>  

Projekt wykonany w ramach kursu **Kodilla – Moduł 9: Formularze i dane**.