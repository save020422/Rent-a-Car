import flet as ft
from ui import *
from Abtsration import InfoManager, Tourist

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    page.bgcolor = ft.Colors.BLUE_GREY_900

    user_data = InfoManager()

    # Crear turistas
    t1 = Tourist("Ana Pérez", "A123456", "Cuba")
    t2 = Tourist("Luis Gómez", "B987654", "México")
    t3 = Tourist("María Torres", "C456789", "Argentina")

    user_data.turistas.extend([t1, t2, t3])

    # Crear la pestaña de usuarios
    users_tab = torist_seccion(infomanager=user_data)

    # Obtener la tabla desde el contenido de la pestaña
    visual_data_table = users_tab.content.controls[-1]

    # Agregar Tabs a la página
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[users_tab],
        expand=1
    )
    page.add(tabs)

    # Ejecutar import_cincro cuando la página termine de cargar
    def on_load(e):
        visual_data_table.import_cincro(user_data)

    page.on_load = on_load

ft.app(target=main)
