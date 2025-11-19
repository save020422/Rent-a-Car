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

cursor.execute("""
CREATE TABLE IF NOT EXISTS Country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT,
    brand TEXT,
    model TEXT,
    color TEXT,
    kilometers_driven REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CarStatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    status TEXT,
    contract_end_date TEXT,
    FOREIGN KEY(car_id) REFERENCES Car(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS RentalContract (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tourist_id INTEGER,
    car_id INTEGER,
    payment_method TEXT,
    start_date TEXT,
    end_date TEXT,
    extension_days INTEGER,
    with_driver INTEGER,
    total_amount REAL,
    FOREIGN KEY(tourist_id) REFERENCES Tourist(id),
    FOREIGN KEY(car_id) REFERENCES Car(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ContractViolator (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tourist_id INTEGER,
    contract_end_date TEXT,
    actual_return_date TEXT,
    FOREIGN KEY(tourist_id) REFERENCES Tourist(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS BrandModelSummary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    car_count INTEGER,
    total_rental_days INTEGER,
    credit_income REAL,
    check_income REAL,
    cash_income REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CountrySummary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER,
    brand TEXT,
    model TEXT,
    rental_days INTEGER,
    extension_days INTEGER,
    cash_value REAL,
    total_value REAL,
    FOREIGN KEY(country_id) REFERENCES Country(id)
)
""")

# Commit and close

# this class use staticmethod for gestion the tourist class in  data base
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

def add_country(name):
    db_path = os.path.join("SrcDataBase", "database.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Country (name) VALUES (?)
    """, (name,))
    connection.commit()
    connection.close()

class CarsBd:
    
    @staticmethod
    def add_car(cars):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Car (license_plate, brand, model, color, kilometers_driven)
            VALUES (?, ?, ?, ?, ?)
        """, (cars.license_plate, cars.brand, cars.model, cars.color, cars.status))
        connection.commit()
        connection.close()

    @staticmethod
    def add_car_status(car_id, status, contract_end_date=None):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO CarStatus (car_id, status, contract_end_date)
            VALUES (?, ?, ?)
        """, (car_id, status, contract_end_date))
        connection.commit()
        connection.close()


    def add_rental_contract(contrato):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO RentalContract (
                tourist_id, car_id, payment_method, start_date, end_date,
                extension_days, with_driver, total_amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (contrato.tourist_id, contrato.car_id, contrato.payment_method, contrato.start_date, contrato.end_date, contrato.extension_days, int(contrato.with_driver), contrato.total_amount))
        connection.commit()
        connection.close()

def add_contract_violator(tourist_id, contract_end_date, actual_return_date):
    db_path = os.path.join("SrcDataBase", "database.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO ContractViolator (tourist_id, contract_end_date, actual_return_date)
        VALUES (?, ?, ?)
    """, (tourist_id, contract_end_date, actual_return_date))
    connection.commit()
    connection.close()

def add_brand_model_summary(brand, model, car_count, total_rental_days, credit_income, check_income, cash_income):
    db_path = os.path.join("SrcDataBase", "database.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO BrandModelSummary (
            brand, model, car_count, total_rental_days,
            credit_income, check_income, cash_income
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (brand, model, car_count, total_rental_days, credit_income, check_income, cash_income))


def add_country_summary(country_id, brand, model, rental_days, extension_days, cash_value, total_value):
    db_path = os.path.join("SrcDataBase", "database.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO CountrySummary (
            country_id, brand, model, rental_days,
            extension_days, cash_value, total_value
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (country_id, brand, model, rental_days, extension_days, cash_value, total_value))
    connection.commit()
    connection.close()



def add_country_summary(country_id, brand, model, rental_days, extension_days, cash_value, total_value):
    db_path = os.path.join("SrcDataBase", "database.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO CountrySummary (
            country_id, brand, model, rental_days,
            extension_days, cash_value, total_value
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (country_id, brand, model, rental_days, extension_days, cash_value, total_value))
    connection.commit()
    connection.close()


connection.commit()
connection.close()
