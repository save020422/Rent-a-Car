import flet as ft

class Tourist:
    def __init__(self, name="", passport_number="", country=""):
        self.name_ = name
        self.passport_number = passport_number
        self.times_used_cars = 0
        self.total_rental_value = 0.0
        self.country = country


class Car:
    def __init__(self, license_plate, brand, model, color, status):
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

    def add_users(self, page, turista):
        self.turistas.append(turista)
        page.update()
        print("Usuario agregado correctamente")

    def repartir_usuarios(self):
        pass


class SpecialContainer(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bgcolor = ft.Colors.GREY_900



\
class SpecialEntry(ft.TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.border_color = ft.Colors.BLUE_900
        self.text_style = ft.TextStyle(color=ft.Colors.WHITE)
        self.label_style = ft.TextStyle(color=ft.Colors.BLUE_900)
        self.height = 40,
        self.width = 200,
        #self.border_radius=20,
        
        #self.border_width = 2

class AppConfig:
    def __init__(self):
        self.config ={
                        "rad" : 5 
                        }