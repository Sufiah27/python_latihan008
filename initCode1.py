class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


if __name__ == '__main__':
    # Creating an instance of the Person class
    person1 = Person("Alice", 30)

    # Accessing attributes and calling a method
    #print(person1.name)  # Output: Alice
    #print(person1.age)  # Output: 30
    person1.introduce()  # Output: My name is Alice and I am 30 years old.
