class Library:
    def __init__(self, city, street, zip_code, open_hours:str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka: {self.city}, ul. {self.street} {self.zip_code} "
                f"(Godziny otwarcia: {self.open_hours}, Tel: {self.phone})")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name} "
                f"(Zatrudniony: {self.hire_date}, Tel: {self.phone})")


class Student:
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (Indeks: {self.index_number})"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: {self.author_name} {self.author_surname}, "
                f"Data publikacji: {self.publication_date}, {self.number_of_pages} str.\n"
                f"Miejsce: {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n".join([f"    - {str(book)}" for book in self.books])

        return (f"Zamówienie z dnia: ({self.order_date})\n"
                f"{self.employee}\n"
                f"{self.student}\n"
                f"Wypożyczone książki:\n{books_description}\n")

lib1 = Library("Gdańsk", "Wita Stwosza 53", "80-308", "08:00-20:00", "58-111-22-33")
lib2 = Library("Wejherowo", "Kasztelanowa 26", "85-974", "10:00-18:00", "58-968-57-04")

emp1 = Employee("Kwiryniusz", "Mruczysław", "1990-09-06", "1954-09-11", "Gdańsk", "Długa 58", "80-407", "589-689-326")
emp2 = Employee("Marek", "Cwaniak", "2019-08-29", "1975-12-12", "Gdynia", "Rozmarynowa 190", "87-356", "436-257-866")
emp3 = Employee("Wacław", "Mądry", "2024-11-07", "1997-08-30", "Kartuzy", "Wilcza 176", "89-124", "846-379-982")

stud1 = Student("Klaudiusz", "Zyguś", "845789")
stud2 = Student("Cecylia", "Jasło", "848937")
stud3 = Student("Gracja", "Wilczek", "848567")

book1 = Book(lib1, "2023", "Eric", "Mathes", 608)
book2 = Book(lib1, "2000", "Roger", "Penrose", 534)
book3 = Book(lib2, "2025", "Piotr", "Pilarski", 52)
book4 = Book(lib2, "2025", "Maciej", "Kawecki", 409)
book5 = Book(lib1, "2021", "Thomas", "Nagel", 120)

order1 = Order(emp1, stud1, [book1, book2, book5], "2025-11-26")
order2 = Order(emp2, stud3, [book3, book4], "2025-11-05")

print(order1)
print()
print(order2)