import flet as ft
from ui import *
from Abtsration import InfoManager

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    #page.theme_mode = "light"
    page.bgcolor =  ft.Colors.BLUE_GREY_900

    user_data = InfoManager()
   
    page.add(
        ft.Tabs(
            selected_index=0,
            tabs=[torist_seccion(infomanager=user_data)],
            expand=1,
            
        )
    )

ft.app(target=main)
