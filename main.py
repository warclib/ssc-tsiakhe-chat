import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "SSC Tsiakhe Messenger"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # Área de mensajes (Lista desplazable)
    chat_list = ft.ListView(expand=True, spacing=10, padding=20)

    # Función para enviar mensajes
    def send_message(e):
        if input_field.value:
            # Añadimos el mensaje a la lista
            chat_list.controls.append(
                ft.Row([
                    ft.Container(
                        content=ft.Text(input_field.value, color=ft.colors.WHITE),
                        bgcolor=ft.colors.BLUE_700,
                        padding=10,
                        border_radius=15,
                    )
                ], alignment=ft.MainAxisAlignment.END)
            )
            # Limpiamos el campo y actualizamos la interfaz
            input_field.value = ""
            page.update()
            chat_list.scroll_to(offset=-1, duration=300)

    # Campo de texto y botón de envío
    input_field = ft.TextField(
        hint_text="Escribe un mensaje...", 
        expand=True, 
        border_radius=20,
        on_submit=send_message # Permite enviar con la tecla Enter
    )
    
    input_bar = ft.Container(
        content=ft.Row([
            input_field, 
            ft.IconButton(ft.icons.SEND_ROUNDED, on_click=send_message)
        ]),
        padding=10,
        bgcolor=ft.colors.GREY_100
    )

    # Layout de la página
    page.add(
        ft.Container(
            content=ft.Text("SSC Tsiakhe - Chat", weight="bold", size=20), 
            padding=15, 
            bgcolor=ft.colors.BLUE_600, 
            color=ft.colors.WHITE
        ),
        chat_list,
        input_bar
    )

# Ejecución
if __name__ == "__main__":
    ft.app(target=main)
