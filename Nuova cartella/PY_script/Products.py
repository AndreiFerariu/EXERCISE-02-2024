class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = bool(availability)  # Converti l'input in un valore booleano

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Availability: {self.availability}")

class Products:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def display_products(self):
        for product in self.product_list:
            product.display_info()
