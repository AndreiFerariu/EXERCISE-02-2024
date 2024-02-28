from dbmanager import DbManager
import mysql.connector

class Product:

    @staticmethod
    def establish_connection():
        try:
            db_manager = DbManager("localhost", 3306, "ferariu_andrei", "masking.assurance.vitiating.", "ferariu_andrei_DBproducts") #cambia
            return db_manager.connect()
        except mysql.connector.Error as e:
            print("Errore durante la connessione al database:", str(e))

    def __init__(self, id, nome, prezzo, marca):
        self._id = id
        self._nome = nome
        self._prezzo = prezzo
        self._marca = marca
    
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def prezzo(self):
        return self._prezzo

    @property
    def marca(self):
        return self._marca

    @staticmethod
    def get_all():
        try: 
            conn = Product.establish_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            records = cursor.fetchall()
            cursor.close()
            return records
        except mysql.connector.Error as e:
            print("Errore durante la ricerca dei prodotti:", str(e))

    @staticmethod
    def find_by_id(id):
        try:
            conn = Product.establish_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return Product(id=row[0], nome=row[1], prezzo=row[2], marca=row[3])
            else:
                return None
        except mysql.connector.Error as e:
            print("Errore durante la ricerca del prodotto:", str(e))

    @staticmethod
    def create_product(product_data):
        try:
            conn = Product.establish_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (nome, prezzo, marca) VALUES (%s, %s, %s)", (product_data['nome'], product_data['prezzo'], product_data['marca']))
            conn.commit()
            product_id = cursor.lastrowid
            conn.close()
            product_data['id'] = product_id
            return product_data
        except mysql.connector.Error as e:
            print("Errore durante la creazione del prodotto:", str(e))

    def update_product(self, product_data):
        try:
            conn = Product.establish_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET marca = %s, nome = %s, prezzo = %s WHERE id = %s", (product_data['marca'], product_data['nome'], product_data['prezzo'], self.id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'aggiornamento del prodotto:", str(e))

    def delete_product(self):
        try:
            conn = Product.establish_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (self.id,))
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print("Errore durante l'eliminazione del prodotto:", str(e))
