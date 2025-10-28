import flet as ft 

# it 's module is for create the users inteface 

def users_seccion():
       tabs_turistas = ft.Tab(
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
                content=ft.Column(),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )
       return tabs_turistas
  

def cars_seccion():
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
                content=ft.Column(),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )
    return tab_autos 
    pass 

def contrat_seccion():
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
                content=ft.Column(),
                bgcolor=ft.Colors.GREY_200,
                padding=10,
                border_radius=15,
                margin=10
            )
        ])
    )
     return tab_contratos


    