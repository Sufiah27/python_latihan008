class FruitStall:
    def __init__(self, stall_name, available_fruits):
        self.stall_name = stall_name
        self.available_fruits = available_fruits

    def display_fruits(self):
        print(f"{self.stall_name} has the following fruits:")
        for fruit in self.available_fruits:
            print(f"- {fruit}")


if __name__ == '__main__':
    # Create an instance of the FruitStall class
    fruit_stall = FruitStall("Fresh Fruits Stall", ["Apple", "Banana", "Orange", "Mango"])

    # Display the available fruits at the stall
    fruit_stall.display_fruits()
