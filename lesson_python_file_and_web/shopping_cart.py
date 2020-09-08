from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    price: int              # in cents
    weight: int             # in grams
    description: str

@dataclass
class CartEntry:
    product: Product
    amount: int = 1

@dataclass
class ShoppingCart:
    cart: List[CartEntry]

    def find(self, product: Product):
        for i, item in enumerate(self.cart):
            if item.product == product:
                return i  # return index if found
        return -1  # not found

    def add(self, product: Product, amount: int = 1):
        i = self.find(product)
        if i >= 0:
            self.cart[i].amount += amount
        else:
            self.cart.append(CartEntry(product, amount))

    def remove(self, product: Product):
        i = self.find(product)
        if i>=0:
            del self.cart[i]

    def get_number_of_items(self):
        return sum([item.amount for item in self.cart])
    
    def get_total_price(self):
        return sum([item.product.price*item.amount for item in self.cart])
        

hammer = Product("Hammer", 2000, 1000, "Excellent for hitting nails")
nail = Product("Nail", 20, 10, "It is a 6 inch nail")
print(hammer)
cart = ShoppingCart([])
cart.add(hammer)
cart.add(nail, 50)
cart.add(nail, 20)
print("Contents:", cart)
print("Number of items:", cart.get_number_of_items())
print("Total Price:", cart.get_total_price())
cart.remove(nail)
print(cart)

