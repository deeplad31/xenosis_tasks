class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

# Create instances of the Person class
p1 = Person('Deep ', 22) 

# Diaplay details of person
p1.display_details()