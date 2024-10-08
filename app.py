from flet import *
import flet as ft

def main(page: ft.Page):
    
    def visibilidade_da_senha(e):
        txt_senha.password = not txt_senha.password
        icon_eye.icon = ft.icons.VISIBILITY if txt_senha.password else ft.icons.VISIBILITY_OFF
        page.update()

    page.title = "PrepWise"
    txt_titulo = ft.Text('Login', size=30, weight="bold")

    # Centralizando a página toda
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campo de nome completo
    name = ft.TextField(
        label="Informe seu nome completo", 
        text_align=ft.TextAlign.LEFT,
        text_style=ft.TextStyle(size=15, weight="bold"),
        width=310,
        border_radius=10,
    )

    # Campo de email
    txt_email = ft.TextField(
        label="Informe seu email", 
        text_align=ft.TextAlign.LEFT,
        text_style=ft.TextStyle(size=15, weight="bold"),
        width=310,
        border_radius=10,
        color="Blue"
    )

    # Campo de senha
    txt_senha = ft.TextField(
        label="Informe sua senha", 
        text_align=ft.TextAlign.LEFT,
        text_style=ft.TextStyle(size=15, weight="bold"),
        width=270,  # Ligeiramente menor para encaixar o ícone
        border_radius=10,
        max_length=30,
        password=True,  # Esconder a senha por padrão
    )

    # Ícone de visibilidade
    icon_eye = ft.IconButton(
        icon=ft.icons.VISIBILITY,
        on_click=visibilidade_da_senha,
        icon_size=24,  # Ajustando o tamanho do ícone
    )

    # Alinhando o campo de senha e o ícone na mesma linha
    senha_row = ft.Row(
        controls=[txt_senha, icon_eye],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0,  # Para reduzir o espaço entre o campo e o ícone
    )

    # Adicionando os elementos centralizados
    page.add(
        ft.Column(
            controls=[
                txt_titulo,
                name,
                txt_email,
                senha_row  # Campo de senha alinhado com o ícone
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza horizontalmente
        )
    )

ft.app(target=main, host="0.0.0.0", port=8550)
