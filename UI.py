import flet as ft
import Inter 
# Sección de Turistas
def users_seccion():
    name = ft.TextField(label="Nombre del turista", height=40)
    pasaporte =ft.TextField(label="Número de pasaporte", height=40)
    nacionalidad = ft.TextField(label="Número de pasaporte", height=40)
    sub_tabs = ft.Tabs(

        
        tabs=[
            ft.Tab(
                text="Formulario",
                content=ft.Container(
                    height=350,
                    content=ft.Column([
                        name,
                        pasaporte,
                        nacionalidad,
                        
                        ft.Row([
                            ft.ElevatedButton("Agregar",on_click= lambda _ :  Inter.add_users(name_= name,
                                                                                  passaport_= pasaporte,country_= nacionalidad)),
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