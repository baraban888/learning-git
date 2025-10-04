import requests
import csv

# URL API NBP (таблица C = курсы покупки/продажи валют)
url = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"

# Делаем запрос
response = requests.get(url)

if response.status_code == 200:
    data = response.json()   # JSON -> Python (list/dict)

    # Берём список валют
    rates = data[0]["rates"]

    # Сохраняем в CSV с разделителем ;
    with open("rates.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        # Заголовки
        writer.writerow(["currency", "code", "bid", "ask"])

        # Строки с данными
        for r in rates:
            writer.writerow([r["currency"], r["code"], r["bid"], r["ask"]])

    print("✅ Курсы сохранены в rates.csv")

else:
    print("❌ Ошибка запроса:", response.status_code)
