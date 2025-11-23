import flet as ft
import Abtsration as ab
def torist_seccion(infomanager):
    tourist = ab.Tourist()
    tourist.name_ = ft.TextField(label="Nombre del turista", height=40)
    tourist.passport_number = ft.TextField(label="Número de pasaporte", height=40)
    tourist.country = ft.TextField(label="Nacionalidad", height=40)

    visual_data_table = ab.ShowDataTable()
    return ft.Tab(

        #CONFIGURATION OF THE TAB
        text="Users",
        icon=ft.Icons.PEOPLE,
        content=ft.Column(
            controls=[tourist.name_,tourist.passport_number,tourist.country,
                      ft.ElevatedButton(text="Add",icon=ft.Icons.ADD,on_click= lambda _ : visual_data_table.add_data(tourist,infomanager)),
                      visual_data_table
                      ]
        )
       )
        