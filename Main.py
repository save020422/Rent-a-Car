import flet as ft
import Ui
from Abtsration import InfoManager

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    #page.theme_mode = "light"
    page.bgcolor =  ft.Colors.BLUE_GREY_900

    user_data = InfoManager()
   
    page.add(
        ft.Tabs(
            selected_index=0,
            tabs=[Ui.users_seccion(page,user_data), 
                  Ui.contrat_seccion(), 
                  Ui.cars_seccion()],
            expand=1,
            
        )
    )

ft.app(target=main)
