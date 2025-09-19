from faker import Faker

# 1. Класс для визитной карточки
class BusinessCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

    # строковое представление объекта
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

fake = Faker()
cards = []

# 2. Генерация случайных данных
for _ in range(5):
    card = BusinessCard(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=fake.company(),
        position=fake.job(),
        email=fake.email(),
    )
    cards.append(card)

# 3. Вывод как строк (используется __str__)
print("Оригинальный список:")
for card in cards:
    print(card)

# 4. Сортировки
by_first = sorted(cards, key=lambda c: c.first_name.casefold())
by_last = sorted(cards, key=lambda c: c.last_name.casefold())
by_email = sorted(cards, key=lambda c: c.email.casefold())

print("\nСортировка по имени:")
for card in by_first:
    print(card)

print("\nСортировка по фамилии:")
for card in by_last:
    print(card)

print("\nСортировка по e-mail:")
for card in by_email:
    print(card)
