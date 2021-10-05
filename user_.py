class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def set_full_name(self, full_name):
        self.surname, self.name = full_name.split(' ')

user1 = User("Anna", "Popivchak", 22)
user1.set_full_name("Petrov Petr")
print(user1.name, user1.surname)
# Petr Petrov

