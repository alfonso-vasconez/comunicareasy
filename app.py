import flet as ft

def main(page: ft.Page):
    page.title = "Comunicareasy"
    page.padding = 20
    
    # Minimal structure ready for your tabs and cards
    page.add(
        ft.Text("Comunicareasy - Base", size=20, weight=ft.FontWeight.BOLD)
    )

ft.run(main)