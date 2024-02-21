from mysql_connection import MySQLConnection

class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

class ProductManager:
    def __init__(self, connection):
        self.connection = connection

    def create_product(self, product):
        query = f"INSERT INTO Products (name, price, availability) VALUES ('{product.name}', {product.price}, {product.availability})"
        self.connection.execute_query(query)

    def read_products(self):
        query = "SELECT * FROM Products"
        cursor = self.connection.execute_query(query)
        return cursor.fetchall()

    def update_product(self, product):
        query = f"UPDATE Products SET price = {product.price}, availability = {product.availability} WHERE name = '{product.name}'"
        self.connection.execute_query(query)

    def delete_product(self, product_name):
        query = f"DELETE FROM Products WHERE name = '{product_name}'"
        self.connection.execute_query(query)
