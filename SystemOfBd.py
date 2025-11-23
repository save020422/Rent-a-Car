import sqlite3
import os

# Create folder if it doesn't exist
folder_path = "SrcDataBase"
os.makedirs(folder_path, exist_ok=True)

# Path to the database file
db_path = os.path.join(folder_path, "database.db")

# Connect to the database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tourist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    passport_number TEXT,
    times_used_cars INTEGER,
    total_rental_value REAL
)
""")






class TouristBd:

    @staticmethod
    def add_tourist(turista):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Tourist (name, passport_number, times_used_cars, total_rental_value)
            VALUES (?, ?, ?, ?)
        """, (turista.name, turista.passport_number, turista.times_used_cars, turista.nacionalidad))
        connection.commit()
        connection.close()

    @staticmethod
    def delete_tourist():
        pass



connection.commit()
connection.close()
