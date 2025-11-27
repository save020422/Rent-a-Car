import flet as ft
import Abtsration as ab
import time 

def torist_tab(infomanager):
    tourist = ab.Tourist()
    
    # inputs seccion
    tourist.name_ = ab.InputBox(
                label="Nombre del turista",
                height=40,
                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    tourist.passport_number = ab.InputBox(
                label="Número de pasaporte",
                height=40,
                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    tourist.country = ab.InputBox(
                label="Nacionalidad",
                height=40,
                text_style=ft.TextStyle(color=ft.Colors.WHITE),
                label_style=ft.TextStyle(color=ft.Colors.WHITE)
    )

    
    visual_data_table = ab.ShowDataTable()
    visual_data_table.import_cincro(infomanager=infomanager)

  
    #input seccion build
   # Lista de países
    country_list = [
        "Afganistán", "Alemania", "Argentina", "Australia", "Brasil", "Canadá", "Chile", "China",
        "Colombia", "Cuba", "Ecuador", "Egipto", "España", "Estados Unidos", "Francia", "India",
        "Italia", "Japón", "México", "Países Bajos", "Perú", "Reino Unido", "Rusia", "Sudáfrica"
    ]

    # Campo de texto para filtrar países
    country_filter = ab.InputBox(
        label="Buscar país",
        hint_text="Escribe para buscar...",
        on_change=lambda e: update_country_dropdown(e.control.value),
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        height=40
    )

    # Dropdown de países
    country_dropdown = ft.Dropdown(
        label="Selecciona un país",
        options=[ft.dropdown.Option(country) for country in country_list],
        on_change=lambda e: setattr(tourist.country, "value", e.control.value),
        text_style=ft.TextStyle(color=ft.Colors.BLACK),
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        #height=40
    )

    # Campo oculto para almacenar el país seleccionado o escrito
    tourist.country = ft.TextField(
        label="Nacionalidad",
        visible=False
    )

    # Función para actualizar el dropdown según el filtro
    def update_country_dropdown(filter_text):
        filtered = [c for c in country_list if filter_text.lower() in c.lower()]
        country_dropdown.options = [ft.dropdown.Option(c) for c in filtered]
        country_dropdown.update()
    column = ft.Column(
        controls=[
            tourist.name_,
            tourist.passport_number,
            country_dropdown,
            tourist.country,
            #country_filter ,
            
            ft.ElevatedButton(
                text="Add",
                icon=ft.Icons.ADD,
                on_click=lambda _: visual_data_table.add_data(tourist, infomanager)
            ),
            visual_data_table
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #wrap= True,

        alignment= ft.MainAxisAlignment.START,
        scroll="auto",
        expand=True
    )

    # Refrescar tabla al montar
    ''' def on_column_mount(e):
            visual_data_table.import_cincro(infomanager)

        column.on_mount = on_column_mount'''

    # Envolver en fila centrada
    return ft.Tab(
        text="Tourist",
        icon=ft.Icons.PERSON_ADD,
        content=column
    )


