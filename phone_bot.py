from collections import UserDict


class Field:
    """Base class for fields in the address book."""
    def __init__(self, value):
        """Initialize the field with a value."""
        self.value = value

    def __str__(self):
        """Return the string representation."""
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    """Class representing a phone number field."""

    def __init__(self, value: str):
        """Initialize the phone number field with validation"""

        self.number_validation(value)
        super().__init__(value)

    def number_validation(self, value):
        """Validate the phone number.
        Args:
            value (str): The phone number to validate.
        Raises:
            ValueError: If the phone number is not valid.
        """


        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        
        if len(value) < 10 or len(value) > 13:
            raise ValueError("Phone number must be between 10 and 13 digits long")

class Record:
    """Class representing a contact record in the address book."""

    def __init__(self, name: str):
        """Initialize the record with a name and an empty list of phones."""

        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone: str):
        """Add a phone number to the record.
        Args:
            phone (str): The phone number to add.
        """

        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Remove a phone number from the record.
        Args:
            phone (str): The phone number to remove.
        """

        find_phone = self.find_phone(phone)
        self.phones.remove(find_phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        """Edit a phone number in the record.
        Args:
            old_phone (str): The phone number to be replaced.
            new_phone (str): The new phone number to add.
        """

        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str):
        """Find a phone number in the record.
        Args:
            phone (str): The phone number to find.
        Returns:
            Phone: The Phone object if found, otherwise None.
        """

        for p in self.phones:
            if p.value == phone:
                return p
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class representing an address book, which is a collection of records."""

    def add_record(self, record: Record):
        """Add a record to the address book.
        Args:
            record (Record): The record to add.
        """

        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """Find a record by name.
        Args:
            name (str): The name of the record to find.
        Returns:
            Record: The record if found, otherwise raises KeyError.
        """

        return self.data[name]

    def delete(self, name: str):
        """Delete a record by name.
        Args:
            name (str): The name of the record to delete.
        """
    
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