from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do "
              f"{self.first_name} {self.last_name}, {self.position} у {self.company}")


# функция для генерации визиток
def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        if contact_type == BaseContact:
            contact = BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()
            )
        elif contact_type == BusinessContact:
            contact = BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                position=fake.job(),
                company=fake.company(),
                business_phone=fake.phone_number()
            )
        else:
            raise ValueError("Nieznany typ kontaktu")
        contacts.append(contact)
    return contacts


# тест
if __name__ == "__main__":
    base_contacts = create_contacts(BaseContact, 3)
    business_contacts = create_contacts(BusinessContact, 3)

    print("\n--- Konakty osobiste---")
    for c in base_contacts:
        print(c)
        c.contact()
        print("label_length =", c.label_length)
        print()

    print("\n--- Kontakty biznesowe---")
    for c in business_contacts:
        print(c)
        c.contact()
        print("label_length =", c.label_length)
        print()
