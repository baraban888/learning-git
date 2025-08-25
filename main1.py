zakupy = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"]
}
for sklep, produkty in zakupy.items():
    print(f"Idę do {sklep}, kupuję tu następujące rzeczy: {produkty}")

suma = sum(len(produkty) for produkty in zakupy.values())
print(f"W sumie kupuję {suma} produktów.")
