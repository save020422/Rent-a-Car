import flet as ft
from ui import *
from Abtsration import InfoManager, Tourist ,SystemBd

#page_init = [False] 


def main(page: ft.Page):
    # Colores de tema
    tema_claro = ft.Colors.WHITE
    tema_oscuro = ft.Colors.BLUE_GREY_900

    # Estado inicial
    page.title = "Sistema de Alquiler de Autos"
    page.bgcolor = tema_claro  # ← Tema blanco por defecto
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    # Inicializar sistema
    info_manager = InfoManager()
    SystemBd.init_db()
    SystemBd.cargar_turistas(info_manager.turistas)

    # Función para cambiar el tema
    def cambiar_tema(e):
        if page.bgcolor == tema_oscuro:
            page.bgcolor = tema_claro
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.bgcolor = tema_oscuro
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    # Botón para cambiar tema
    boton_tema = ft.Button(
        text="2",
        on_click=cambiar_tema,
        bgcolor=ft.Colors.BLUE_200,
        color=ft.Colors.BLACK,
        icon= ft.Icons.DARK_MODE_OUTLINED,
        width= 50 ,
        height= 30
    )

    # Tabs principales
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            torist_seccion(infomanager=info_manager),
            cars_seccion(infomanager=info_manager),
            Contrat_seccion(infomanager=info_manager)
        ],
        expand=1,
        animation_duration=200
    )

    # Agregar controles a la página
    page.add(boton_tema, tabs)
    page.update()

# Ejecutar la app
ft.app(target=main)
