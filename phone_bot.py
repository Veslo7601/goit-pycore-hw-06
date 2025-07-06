from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value: str):
        self.number_validation(value)
        super().__init__(value)

    def number_validation(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        
        if len(value) < 10 or len(value) > 13:
            raise ValueError("Phone number must be between 10 and 13 digits long")

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        find_phone = self.find_phone(phone)
        self.phones.remove(find_phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str):
        self.data.pop(name)



# Example usage
if __name__ == "__main__":
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")