import sqlite3

# It's for managing the database

connection = sqlite3.connect("database.db")  

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        name TEXT,
        number_ticket INT,
        number_use INT,
        total_value_of_rents INT
    )
""")

connection.commit()
connection.close()
