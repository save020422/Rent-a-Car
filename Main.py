import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Alquiler de Autos"
    page.theme_mode = "light"

    # Ejemplo de datos agregados (puedes conectar con una base de datos luego)
    turistas = [
        ft.Text("Ana Torres - Pasaporte: 123456 - Veces: 2 - Total: $500"),
        ft.Text("Luis Gómez - Pasaporte: 789012 - Veces: 1 - Total: $300")
    ]

    autos = [
        ft.Text("Placa: ABC123 - Toyota Corolla - Rojo - 15,000 km"),
        ft.Text("Placa: XYZ789 - Kia Rio - Azul - 8,000 km")
    ]

    contratos = [
        ft.Text("Ana Torres - ABC123 - Efectivo - 2023-01-01 a 2023-01-05 - Chofer: No - Total: $500"),
        ft.Text("Luis Gómez - XYZ789 - Tarjeta - 2023-02-01 a 2023-02-03 - Chofer: Sí - Total: $300")
    ]

    # 🧍 Turistas
    tab_turistas = ft.Tab(
        text="Turistas",
        content=ft.Column([
            ft.Text("Gestión de Turistas", size=20, weight="bold"),
            ft.TextField(label="Nombre del turista"),
            ft.TextField(label="Número de pasaporte"),
            ft.Row([
                ft.ElevatedButton("Agregar"),
                ft.ElevatedButton("Editar"),
                ft.ElevatedButton("Eliminar"),
            ]),
            ft.Container(
                content=ft.Column(turistas),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )

    # 🚗 Autos
    tab_autos = ft.Tab(
        text="Autos",
        content=ft.Column([
            ft.Text("Gestión de Autos", size=20, weight="bold"),
            ft.TextField(label="Placa"),
            ft.TextField(label="Marca"),
            ft.TextField(label="Modelo"),
            ft.TextField(label="Color"),
            ft.TextField(label="Kilómetros recorridos"),
            ft.Row([
                ft.ElevatedButton("Agregar"),
                ft.ElevatedButton("Editar"),
                ft.ElevatedButton("Eliminar"),
            ]),
            ft.Container(
                content=ft.Column(autos),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )

    # 📄 Contratos
    tab_contratos = ft.Tab(
        text="Contratos",
        content=ft.Column([
            ft.Text("Gestión de Contratos", size=20, weight="bold"),
            ft.TextField(label="Nombre del turista"),
            ft.TextField(label="Placa del auto"),
            ft.TextField(label="Forma de pago"),
            ft.TextField(label="Fecha inicio"),
            ft.TextField(label="Fecha fin"),
            ft.TextField(label="Prórroga (días)"),
            ft.Switch(label="Alquiler de chofer"),
            ft.TextField(label="Importe total"),
            ft.Row([
                ft.ElevatedButton("Agregar"),
                ft.ElevatedButton("Editar"),
                ft.ElevatedButton("Eliminar"),
            ]),
            ft.Container(
                content=ft.Column(contratos),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )

    # 🗂️ Tabs principales
    page.add(
        ft.Tabs(
            selected_index=0,
            tabs=[tab_turistas, tab_autos, tab_contratos],
            expand=1
        )
    )

ft.app(target=main)
