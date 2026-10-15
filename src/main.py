import flet as ft
from models.data_manager import DataManager

def main(page: ft.Page):
    page.title = "Comunicareasy - SAAC"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START

    # 1. Inicializamos el gestor de datos
    data_manager = DataManager()
    
    # 2. Obtenemos el paciente actual y sus rutinas
    patient = data_manager.get_current_patient()
    patient_name = patient.get("name", "Paciente")
    
    routines = data_manager.get_routines()
    
    # Título principal de la app con el nombre del paciente
    header_text = ft.Text(
        f"Comunicación para: {patient_name}", 
        size=24, 
        weight=ft.FontWeight.BOLD
    )
    
    # Contenedor dinámico de la cuadrícula
    cards_grid = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=200,
        child_aspect_ratio=1.0,
        spacing=15,
        run_spacing=15,
    )

    # 3. Cargamos las tarjetas de la primera categoría
    if routines:
        categories = routines[0].get("categories", [])
        if categories:
            cards_data = categories[0].get("cards", [])
            
            for card in cards_data:
                title = card.get("title", "")
                
                # Mapeo seguro de iconos predeterminados basados en el JSON
                icon_key = card.get("icon", "help").upper()
                # Buscamos de forma dinámica en ft.Icons o caemos en un icono por defecto
                icon_enum = getattr(ft.Icons, icon_key, ft.Icons.HELP)
                
                # Tarjeta visual con el Icon corregido
                card_button = ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(icon=icon_enum, size=40, color=ft.Colors.WHITE),
                            ft.Text(
                                title, 
                                size=16, 
                                weight=ft.FontWeight.BOLD, 
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=ft.Colors.BLUE_700,
                    border_radius=12,
                    padding=15,
                    ink=True,
                    on_click=lambda e, t=title: print(f"Reproduciendo voz para: {t}")
                )
                cards_grid.controls.append(card_button)

    # Añadimos los elementos a la página
    page.add(
        header_text,
        ft.Divider(height=20),
        cards_grid
    )

ft.run(main)