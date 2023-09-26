class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Get user input for name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

if __name__ == '__main__':
    # Create a Person object with user-input data
    person = Person(name, age)

    # Display the information
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
