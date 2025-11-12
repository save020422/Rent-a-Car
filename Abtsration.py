

class Tourist:
    def __init__(self, name ="", passport_number = "",country = ""):
        self.name_ = name
        self.passport_number = passport_number
        self.times_used_cars = 0
        self.total_rental_value = 0.0
        self.country = country




class Car:
    def __init__(self, license_plate, brand, model, color,status):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.color = color
        self.kilometers_driven = 0
        self.carstatus = status





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
    

class InfoManager:
    def __init__(self):
        self.turistas = []
        self.autos = []
        self.contratos = []
        
        
        pass

