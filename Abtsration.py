import flet as ft

class Tourist:
    def __init__(self, name ="", passport_number = "",country = ""):
        self.name = name
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



class ShowDataTable(ft.DataTable):
    def __init__(self, **kwargs):
        columns = [
            ft.DataColumn(ft.Text("passport_number", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("name", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("country", color=ft.Colors.WHITE))
        ]

        super().__init__(
            columns=columns,
            border=ft.border.all(1, ft.Colors.GREY),
            border_radius=12,
            vertical_lines= ft.border.BorderSide(1, ft.Colors.GREY),
            #data_row_color={"even": ft.Colors.BLUE_50, "odd": ft.Colors.WHITE},
            divider_thickness=1,
            column_spacing=20,
            #heading_row_color=ft.Colors.BLUE_200,
            **kwargs
        )

        #self.width = 10 # Limita el ancho de la tabla
        #self.bgcolor = ft.Colors.BLUE_100
