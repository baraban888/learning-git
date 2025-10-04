# Zadanie: Kursy walut NBP

Projekt w ramach bootcampu **Kodilla**.  
Celem było:

1. Pobranie danych z API Narodowego Banku Polskiego (NBP) w formacie JSON.  
2. Utworzenie pliku CSV zawierającego listę walut (kolumny: `currency;code;bid;ask`).  
3. Stworzenie prostego kalkulatora walut w HTML/JS, korzystającego z danych NBP.  

---

## 📂 Struktura projektu

learning-git-task/
│── nbp_to_csv.py # skrypt Python do pobierania kursów i zapisu w CSV
│── rates.csv # wygenerowany plik CSV z kursami
│── index.html # kalkulator walut (PL/UA)
│── requirements.txt # zależności Pythona (requests)

---

## ⚙️ Uruchamianie skryptu

1. Aktywuj wirtualne środowisko:

   ```bash
   source venv/Scripts/activate   # Windows Git Bash

Uruchom skrypt:

python nbp_to_csv.py


W projekcie pojawi się plik rates.csv z danymi w formacie:

currency;code;bid;ask
dolar amerykański;USD;4.2154;4.3002
jen (Japonia);JPY;0.0241;0.0249
frank szwajcarski;CHF;4.5047;4.5957
...

💻 Kalkulator walut

Otwórz plik index.html w przeglądarce.

Wybierz walutę z listy.

Podaj ilość.

Wybierz operację:

Kupić (PLN → waluta)

Sprzedać (waluta → PLN)

Kliknij przycisk Przelicz.

Kalkulator działa w dwóch wersjach językowych (PL / UA) z przełącznikiem w prawym górnym rogu.

📦 Zależności

Python:

requests

Instalacja:

pip install -r requirements.txt

📌 Źródło danych

API NBP (Tabela C):
 [https://api.nbp.pl/api/exchangerates/tables/C?format=json]

 ---

## 👤 Autor

Alex Bahatiuk  
📧 [1975bahat@gmail.com]  
🌐 [github.com/baraban888](https://github.com/baraban888)
