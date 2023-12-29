
class Product:
    def __init__(self, name, id, price, rating, stock):
        self.name = name
        self.id = id
        self.price = price
        self.rating = rating
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        self.stock -= quantity

    def update_rating(self, new_rating):
        self.rating = new_rating

    def update_price(self, new_price):
        self.price = new_price


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        self.products.remove(product)

    def get_item(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None


class Basket:
    def __init__(self):
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        self.products.remove(product)

    def get_item(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def make_purchase(self, ids):
        purchased_products = []
        for id in ids:
            for product in self.products:
                if product.id == id:
                    purchased_products.append(product)
                    self.products.remove(product)
                    break
        for product in purchased_products:
            print(f"Purchased: {product.name}")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket = Basket()



product1 = Product("Product1", 1, 10.0, 4.5, 100)
product2 = Product("Product2", 2, 15.0, 4.0, 50)

category1 = Category("Category1")
category1.add_item(product1)
category1.add_item(product2)

user1 = User("user1", "password1")
user2 = User("user2", "password2")