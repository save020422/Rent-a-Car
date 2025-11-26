import flet as ft
import Abtsration as ab  # Asegúrate de que este módulo esté bien definido

def tourist_tab():
    tourist = ab.Tourist()

    # Campos de entrada estilizados
    tourist.name_ = ft.FilledButton(
        text ="Nombre del turista",
        height=40,
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    tourist.passport_number = ft.FilledButton(
        text ="Número de pasaporte",
        height=40,
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    tourist.country = ft.FilledButton(
        text ="Nacionalidad",
        height=40,
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    def add_tourist(e):
        print("Nombre:", tourist.name_.value)
        print("Pasaporte:", tourist.passport_number.value)
        print("Nacionalidad:", tourist.country.value)

    column = ft.Column(
        controls=[
            tourist.name_,
            tourist.passport_number,
            tourist.country,
            ft.ElevatedButton(
                text="Agregar",
                icon=ft.Icons.ADD,
                on_click=add_tourist
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        scroll="auto",
        expand=True
    )

    return ft.Tab(
        text="Turista",
        icon=ft.Icons.PERSON_ADD,
        content=ft.Row(
            controls=[column],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
            expand=True
        )
    )


def main(page: ft.Page):
    page.title = "Registro de Turistas"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(ft.Tabs(tabs=[tourist_tab()]))

ft.app(target=main)
