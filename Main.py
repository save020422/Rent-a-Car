import flet as ft
import time
import threading

def show_main_ui(page: ft.Page):
    # --- Tourists Tab ---
    tourist_name = ft.TextField(label="Name")
    passport_number = ft.TextField(label="Passport Number")
    add_tourist_btn = ft.ElevatedButton("Add Tourist")

    tourist_tab = ft.Column([
        ft.Text("Add Tourist", size=20, weight="bold"),
        tourist_name,
        passport_number,
        add_tourist_btn
    ])

    # --- Cars Tab ---
    license_plate = ft.TextField(label="License Plate")
    brand = ft.TextField(label="Brand")
    model = ft.TextField(label="Model")
    color = ft.TextField(label="Color")
    add_car_btn = ft.ElevatedButton("Add Car")

    car_tab = ft.Column([
        ft.Text("Add Car", size=20, weight="bold"),
        license_plate,
        brand,
        model,
        color,
        add_car_btn
    ])

    # --- Contracts Tab ---
    tourist_id = ft.TextField(label="Tourist ID")
    car_id = ft.TextField(label="Car ID")
    payment_method = ft.Dropdown(
        label="Payment Method",
        options=[
            ft.dropdown.Option("cash"),
            ft.dropdown.Option("check"),
            ft.dropdown.Option("credit_card")
        ]
    )
    start_date = ft.TextField(label="Start Date (YYYY-MM-DD)")
    end_date = ft.TextField(label="End Date (YYYY-MM-DD)")
    extension_days = ft.TextField(label="Extension Days")
    with_driver = ft.Switch(label="With Driver")
    total_amount = ft.TextField(label="Total Amount")
    add_contract_btn = ft.ElevatedButton("Add Contract")

    contract_tab = ft.Column([
        ft.Text("Add Rental Contract", size=20, weight="bold"),
        tourist_id,
        car_id,
        payment_method,
        start_date,
        end_date,
        extension_days,
        with_driver,
        total_amount,
        add_contract_btn
    ])

    # --- Tabs Layout ---
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Tourists", content=tourist_tab),
            ft.Tab(text="Cars", content=car_tab),
            ft.Tab(text="Contracts", content=contract_tab)
        ],
        expand=True
    )

    page.controls.clear()
    page.add(tabs)
    page.update()

def main(page: ft.Page):
    page.title = "Rent a Car"
    page.bgcolor = ft.Colors.YELLOW
    splash = ft.Text("Rent a Car", size=40, weight="bold", color=ft.Colors.BLUE_600)
    page.add(
        ft.Column(
            [splash],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    def delayed_start():
        time.sleep(3)
        show_main_ui(page)

    threading.Thread(target=delayed_start).start()

ft.app(target=main)
