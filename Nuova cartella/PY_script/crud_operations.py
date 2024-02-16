from DB_connection import MySQLConnection

class CRUDOperations:
    def __init__(self, host, user, password, database):
        self.db_manager = MySQLConnection(host, user, password, database)
        self.db_manager.connect()

    def create(self, table, **data):
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.db_manager.execute_query(query)

    def read(self, table, conditions=None):
        query = f"SELECT * FROM {table}"
        if conditions:
            query += f" WHERE {conditions}"
        self.db_manager.execute_query(query)
        rows = self.db_manager.cursor.fetchall()
        return rows

    def update(self, table, set_values, conditions=None):
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in set_values.items()])
        query = f"UPDATE {table} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"
        self.db_manager.execute_query(query)

    def delete(self, table, conditions=None):
        query = f"DELETE FROM {table}"
        if conditions:
            query += f" WHERE {conditions}"
        self.db_manager.execute_query(query)

    def close_connection(self):
        self.db_manager.close_connection()
