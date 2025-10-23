# 🧍‍♂️ Tourist

class Tourist:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
        self.times_used_cars = 0
        self.total_rental_value = 0.0

class Country:
    def __init__(self, name):
        self.name = name
        self.tourists = []

    def add_tourist(self, tourist):
        self.tourists.append(tourist)

# 🚗 Car
class Car:
    def __init__(self, license_plate, brand, model, color):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.color = color
        self.kilometers_driven = 0


class CarStatus:
    def __init__(self, car, status, contract_end_date=None):
        self.car = car
        self.status = status  # 'available', 'rented', 'in_repair'
        self.contract_end_date = contract_end_date


class RentalContract:
    def __init__(self, tourist, car, payment_method, start_date, end_date, extension_days, with_driver, total_amount):
        self.tourist = tourist
        self.car = car
        self.payment_method = payment_method  # 'cash', 'check', 'credit_card'
        self.start_date = start_date
        self.end_date = end_date
        self.extension_days = extension_days
        self.with_driver = with_driver
        self.total_amount = total_amount


class ContractViolator:
    def __init__(self, tourist, contract_end_date, actual_return_date):
        self.tourist = tourist
        self.contract_end_date = contract_end_date
        self.actual_return_date = actual_return_date

    def is_violation(self):
        return self.actual_return_date > self.contract_end_date

# 📈 Brand & Model Summary
class BrandModelSummary:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.car_count = 0
        self.total_rental_days = 0
        self.credit_income = 0.0
        self.check_income = 0.0
        self.cash_income = 0.0

    def total_income(self):
        return self.credit_income + self.check_income + self.cash_income

# 🌐 Country Summary
class CountrySummary:
    def __init__(self, country):
        self.country = country
        self.brand_model_data = {}  # {(brand, model): data}

    def add_data(self, brand, model, rental_days, extension_days, cash_value, total_value):
        key = (brand, model)
        if key not in self.brand_model_data:
            self.brand_model_data[key] = {
                'rental_days': 0,
                'extension_days': 0,
                'cash_value': 0.0,
                'total_value': 0.0
            }
        self.brand_model_data[key]['rental_days'] += rental_days
        self.brand_model_data[key]['extension_days'] += extension_days
        self.brand_model_data[key]['cash_value'] += cash_value
        self.brand_model_data[key]['total_value'] += total_value
