import flet as ft
import Ui

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    page.theme_mode = "light"

      
   
    page.add(
        ft.Tabs(
            selected_index=0,
            tabs=[Ui.users_seccion(), Ui.contrat_seccion(), Ui.cars_seccion()],
            expand=1
        )
    )

ft.app(target=main)
