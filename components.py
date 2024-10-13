# components.py
import flet as ft

def criar_campo_senha(label, senha_textfield, icone_click_handler):
    """
    Função que cria um campo de senha com ícone de visibilidade.
    """
    senha_textfield = ft.TextField(
        label=label, 
        text_align=ft.TextAlign.LEFT,
        text_style=ft.TextStyle(size=15, weight="bold"),
        width=260,  # Ligeiramente menor para encaixar o ícone
        border_radius=10,
        max_length=30,
        password=True,  # Esconder a senha por padrão
    )
    icon_eye = ft.IconButton(
        icon=ft.icons.VISIBILITY_OFF,  # Começa com o ícone de olho fechado
        on_click=icone_click_handler
    )

    # Retorna uma linha contendo o campo de senha e o ícone
    return ft.Row(
        controls=[senha_textfield, icon_eye],
        alignment=ft.MainAxisAlignment.CENTER
    )
