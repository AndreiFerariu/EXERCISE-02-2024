import mysql.connector

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connessione al database avvenuta con successo!")
        except mysql.connector.Error as e:
            print(f"Errore durante la connessione al database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query eseguita con successo!")
        except mysql.connector.Error as e:
            print(f"Errore durante l'esecuzione della query: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connessione al database chiusa.")



