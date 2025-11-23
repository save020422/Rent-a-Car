import flet as ft
from ui import *
from Abtsration import InfoManager, Tourist
import SystemOfBd as bd
#page_init = [False] 

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    page.bgcolor = ft.Colors.BLUE_GREY_900

    user_data = InfoManager()
    bd.init()
    bd.TouristBD.insertar_turistas_demo()
    bd.TouristBD.cargar_turistas(user_data.turistas)

    

    # Crear turistas
    t1 = Tourist("Ana Pérez", "A123456", "Cuba")
    t2 = Tourist("Luis Gómez", "B987654", "México")
    t3 = Tourist("María Torres", "C456789", "Argentina")

    user_data.turistas.extend([t1, t2, t3])

    # Crear la pestaña de usuarios
    users_tab = torist_seccion(infomanager=user_data )

    # Obtener la tabla desde el contenido de la pestaña
    #visual_data_table = users_tab.content.controls[-1]

    # Agregar Tabs a la página 
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[users_tab],
        expand=1
    )
    page.add(tabs)
    page.update()

    #page_init[0] = True
    # Ejecutar import_cincro cuando la página termine de cargar
    

ft.app(target=main)
