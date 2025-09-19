from faker import Faker

class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    # 1. Метод contact()
    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}, "
              f"{self.position}, {self.email}")

    # 2. Динамический атрибут (property)
    @property
    def name_length(self):
        return len(self.first_name) + len(self.last_name)


# Тест
fake = Faker()
cards = []

for _ in range(3):
    card = BusinessCard(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=fake.company(),
        position=fake.job(),
        email=fake.email(),
    )
    cards.append(card)

# Проверяем
for card in cards:
    print(card)             # сработает __str__
    card.contact()          # вызов метода contact()
    print("Suma długości imienia i nazwiska:", card.name_length)
    print()
