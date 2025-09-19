from faker import Faker

# 1. Клас для візитної картки
class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

# 2. Генерація випадкових даних
fake = Faker()
cards = []

for _ in range(5):
    card = BusinessCard(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=fake.company(),
        position=fake.job(),
        email=fake.email()
    )
    cards.append(card)

# 3. Вивід у зручному форматі
for card in cards:
    print(f"{card.first_name} {card.last_name} - {card.email}")
