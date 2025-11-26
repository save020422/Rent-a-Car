import flet as ft
import os
import sqlite3

class Tourist:
    def __init__(self, name="", passport_number="", country=""):
        self.name = name
        self.passport_number = passport_number
        self.country = country


class SystemBd:
    @staticmethod
    def init_db():
        os.makedirs("SrcDataBase", exist_ok=True)
        db_path = os.path.join("SrcDataBase", "database.db")

        if os.path.exists(db_path):
            print(f"Base de datos encontrada en: {db_path}")
            print("Usando la base de datos existente.")
        else:
            print("Creando nueva base de datos.")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tourist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            passport_number TEXT,
            country TEXT
        )
        """)

        conn.commit()
        conn.close()

    @staticmethod
    def cargar_turistas(tourists_list):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT name, passport_number, country FROM Tourist")
            for row in cursor.fetchall():
                t = Tourist(name=row[0], passport_number=row[1], country=row[2])
                tourists_list.append(t)
        except sqlite3.Error as e:
            print(f"Error al cargar turistas: {e}")
        finally:
            connection.close()

    @staticmethod
    def insertar_turistas_demo():
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        turistas_demo = [
                Tourist(name="Elizabeth Windsor", passport_number="G445566", country="Inglaterra"),
                Tourist(name="Dwayne Campbell", passport_number="F998877", country="Jamaica"),
                Tourist(name="Jean-Pierre Tremblay", passport_number="H778899", country="Canadá"),
                Tourist(name="Aiko Tanaka", passport_number="I334455", country="Japón"),
                Tourist(name="Li Wei", passport_number="J667788", country="China")
                ]

        try:
            for t in turistas_demo:
                cursor.execute("""
                    INSERT OR IGNORE INTO Tourist (name, passport_number, country)
                    VALUES (?, ?, ?)
                """, (t.name, t.passport_number, t.country))
            connection.commit()
            print("Turistas de prueba insertados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar turistas demo: {e}")
        finally:
            connection.close()

    @staticmethod
    def insertar_turista(turista):
        db_path = os.path.join("SrcDataBase", "database.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO Tourist (name, passport_number, country)
                VALUES (?, ?, ?)
            """, (turista.name, turista.passport_number, turista.country))
            connection.commit()
            print(f"Turista '{turista.name}' insertado correctamente.")
        except sqlite3.IntegrityError:
            print(f"El turista con pasaporte '{turista.passport_number}' ya existe. No se insertó.")
        except sqlite3.Error as e:
            print(f"Error al insertar turista: {e}")
        finally:
            connection.close()









class Car:
    def __init__(self, license_plate ="" , brand ="", model ="", color =" ",status=" "):
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
            ft.DataColumn(ft.Text("passport_number")),
            ft.DataColumn(ft.Text("name")),
            ft.DataColumn(ft.Text("country"))
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

    def add_data(self, entidad,infomanager = ""):
    # Asegúrate de que 'entidad' tenga los atributos necesarios
        new_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(entidad.passport_number.value)),
                ft.DataCell(ft.Text(entidad.name_.value)),
                ft.DataCell(ft.Text(entidad.country.value))
            ]
        )
        tourits = Tourist(name=entidad.name_.value,
                          passport_number=entidad.passport_number.value,
                          country=entidad.country.value)
        
        SystemBd.insertar_turista(tourits)
        
                          
        
        entidad.passport_number.value = entidad.name_.value =  entidad.country.value = ""
        entidad.name_.update()
        entidad.passport_number.update()
        entidad.country.update()

        infomanager.turistas.append(tourits)
        


        
        self.rows.append(new_row)
        self.update()
    
    def import_cincro(self, infomanager):
        for turista in infomanager.turistas:
            new_row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(turista.passport_number)),
                    ft.DataCell(ft.Text(turista.name)),
                    ft.DataCell(ft.Text(turista.country))
                ]
            )
            self.rows.append(new_row)
        #self.update()

class MyColum(ft.Column):
    def __init__(self, controls = None, alignment = None, horizontal_alignment = None, spacing = None, tight = None, wrap = None, run_spacing = None, run_alignment = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, visible = None, disabled = None, data = None, rtl = None, scroll = None, auto_scroll = None, on_scroll_interval = None, on_scroll = None, adaptive = None):
        super().__init__(controls, alignment, horizontal_alignment, spacing, tight, wrap, run_spacing, run_alignment, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, rtl, scroll, auto_scroll, on_scroll_interval, on_scroll, adaptive)
    pass

    def auto_center():
        pass
      
class InputBox(ft.TextField):
    def __init__(self,label ="",**kwargs):
        super().__init__(text_align=ft.TextAlign.CENTER,label="",
                height=30,width=300)
        self.label = label


class SwitsButton(ft.Button):
    def __init__(self, text = None,page= None, **kwargs):
       

       super().__init__(text, icon = ft.Icons.LIGHT_MODE,
                        on_click= lambda _: self.theme_change())
       self.page = page
       
       
       
    def theme_change(self):
            
            if self.page.theme_mode == ft.ThemeMode.LIGHT:
                self.page.theme_mode = ft.ThemeMode.DARK
            else:
                self.page.theme_mode = ft.ThemeMode.LIGHT
                pass


class QuestCountry():
    pass

