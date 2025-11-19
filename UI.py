import flet as ft
from Abtsration import Tourist , SpecialContainer, SpecialEntry
# Sección de Turistas
def users_seccion(page,user_data  = ""):
    rad = int(10)
    tourist_entry = Tourist()
    tourist_entry.name = SpecialEntry(label="Nombre del turista", height=40 ,border_radius=rad)
    tourist_entry.pasaporte = SpecialEntry(label="Número de pasaporte", height=40,border_radius=rad)
    tourist_entry.nacionalidad = SpecialEntry(label="Nacionalidad", height=40,border_radius=rad)

    datos = ["Turista 1", "Turista 2", "Turista 3"]  # Asegúrate de definir 'datos'

    sub_tabs = ft.Tabs(
        tabs=[
            ft.Tab(
                text="Formulario",
                content=ft.Container(
                    height=350,
                    content=ft.Column([
                        tourist_entry.name,
                        tourist_entry.pasaporte,
                        tourist_entry.nacionalidad,
                        ft.Row([
                            ft.ElevatedButton("Agregar", on_click=lambda _: user_data.add_users(tourist_entry)),
                            ft.ElevatedButton("Editar"),
                            ft.ElevatedButton("Eliminar"),
                        ]),
                        ft.Container(
                            content=ft.Column(),
                            bgcolor=ft.Colors.GREY_200,
                            padding=5,
                            border_radius=10,
                            margin=5
                        )
                    ], scroll="auto")
                )
            ),
            ft.Tab(
                text="Listado",
                content=SpecialContainer(
                    content=ft.Column([
                        ft.Text("Listado"),
                        ft.Column(
                            controls=[ft.Text(user_data.turistas) for item in datos]
                        )
                    ]),
                    bgcolor=ft.Colors.GREY_100,
                    padding=10,
                    border_radius=10
                )
            )
        ]
    )

    return ft.Tab(text="Turistas", content=sub_tabs)




def contrat_seccion():
    sub_tabs = ft.Tabs(
        tabs=[
            ft.Tab(text="Formulario",
                content=ft.Container(
                    height=400,
                    content=ft.Column([
                        ft.Text("Gestión de Contratos", size=18, weight="bold"),
                        ft.TextField(label="Nombre del turista", height=40),
                        ft.TextField(label="Placa del auto", height=40),
                        ft.TextField(label="Forma de pago", height=40),
                        ft.TextField(label="Fecha inicio", height=40),
                        ft.TextField(label="Fecha fin", height=40),
                        ft.TextField(label="Prórroga (días)", height=40),
                        ft.Switch(label="Alquiler de chofer"),
                        ft.TextField(label="Importe total", height=40),
                        ft.Row([
                            ft.ElevatedButton("Agregar"),
                            ft.ElevatedButton("Editar"),
                            ft.ElevatedButton("Eliminar"),
                        ]),
                        ft.Container(
                            content=ft.Column(),
                            bgcolor=ft.Colors.GREY_200,
                            padding=5,
                            border_radius=10,
                            margin=5
                        )
                    ], scroll="auto")
                )
            ),
            ft.Tab(
                text="Listado",
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Listado")
                    ]),
                    bgcolor=ft.Colors.GREY_100,
                    padding=10,
                    border_radius=10
                )
            )
        ]
    )
    return ft.Tab(text="Contratos", content=sub_tabs)

def cars_seccion():
    sub_tabs = ft.Tabs(
        tabs=[
            ft.Tab(
                text="Formulario",
                content=ft.Container(
                    height=400,
                    content=ft.Column([
                        ft.Text("Gestión de Autos", size=18, weight="bold"),
                        ft.TextField(label="Placa", height=40),
                        ft.TextField(label="Marca", height=40),
                        ft.TextField(label="Modelo", height=40),
                        ft.TextField(label="Color", height=40),
                        ft.TextField(label="Kilómetros recorridos", height=40),
                        ft.Row([
                            ft.ElevatedButton("Agregar"),
                            ft.ElevatedButton("Editar"),
                            ft.ElevatedButton("Eliminar"),
                        ]),
                        ft.Container(
                            content=ft.Column(),
                            bgcolor=ft.Colors.GREY_200,
                            padding=5,
                            border_radius=10,
                            margin=5
                        )
                    ], scroll="auto")
                )
            ),
            ft.Tab(
                text="Listado",
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Listado")
                    ]),
                    bgcolor=ft.Colors.GREY_100,
                    padding=10,
                    border_radius=10
                )
            )
        ]
    )
    return ft.Tab(text="Autos", content=sub_tabs)