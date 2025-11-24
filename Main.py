import flet as ft
from ui import *
from Abtsration import InfoManager, Tourist ,SystemBd

#page_init = [False] 

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    #bd =SystemBd
    info_manager = InfoManager()
    SystemBd.init_db()
   # SystemBd.insertar_turistas_demo()
    SystemBd.cargar_turistas(info_manager.turistas)

    

    #

    # Crear la pestaña de usuarios
    

    # Obtener la tabla desde el contenido de la pestaña
    #visual_data_table = users_tab.content.controls[-1]

    # Agregar Tabs a la página 
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[torist_seccion(infomanager=info_manager ),
              cars_seccion(infomanager=info_manager),
              Contrat_seccion(infomanager=info_manager)],
        expand=1,
        animation_duration= 200
    )
    page.add(tabs)
    page.update()

    #page_init[0] = True
    # Ejecutar import_cincro cuando la página termine de cargar
    

ft.app(target=main)
