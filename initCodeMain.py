class Food:
    def __init__(self, stall_name, foodlist):
        #__init__ - allow user to freely use the parameter by giving them a value that can be used in other line
        self.stall_name = stall_name
        self.foodlist = foodlist
        self.order = []

    def displayFood(self):
        print(f"{self.stall_name} Menu: ")
        for i, food in enumerate(self.foodlist, start=1):
            print(f"{i}) {food}")

    def takeOrder(self):
        order_numbers = input("Enter your order numbers separated by spaces: ").split()
        for num in order_numbers:
            num = int(num)
            if num >= 1 and num <= len(self.foodlist):
                self.order.append(self.foodlist[num - 1])
            else:
                print(f"Invalid order number: {num}")

    def displayOrder(self):
        if self.order:
            print("\nYour order:")
            for i, food in enumerate(self.order, start=1):
                print(f"{i}) {food}")
        else:
            print("You haven't placed any orders yet.")

if __name__ == '__main__':
    food_stall = Food("Fingerlicking-Good", ["Nasi Lemak", "Nasi Kerabu", "Nasi Lauk Ayam"])

    food_stall.displayFood()
    food_stall.takeOrder()
    food_stall.displayOrder()
