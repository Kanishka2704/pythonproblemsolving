class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity):
        self.items.append({'item_name': item_name, 'price': price, 'quantity': quantity})
        print(f"Added {quantity} {item_name}(s) to the cart.")

    def remove_item(self, item_name, quantity):
        for item in self.items:
            if item['item_name'] == item_name:
                if item['quantity'] <= quantity:
                    self.items.remove(item)
                    print(f"Removed {item['quantity']} {item_name}(s) from the cart.")
                else:
                    item['quantity'] -= quantity
                    print(f"Removed {quantity} {item_name}(s) from the cart.")
                return
        print(f"{item_name} not found in the cart.")

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        print(f"Total price of items in the cart: ${total:.2f}")

# Example usage
cart = ShoppingCart()

# Adding items
cart.add_item("Apple", 0.50, 5)


# Removing items
cart.remove_item("Apple", 2)


# Calculating total
cart.calculate_total()
