import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Connessione al database avvenuta con successo!")
        except sqlite3.Error as e:
            print(f"Errore durante la connessione al database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query eseguita con successo!")
        except sqlite3.Error as e:
            print(f"Errore durante l'esecuzione della query: {e}")


