# views.py
import flet as ft

def tela_login(page, senha_row):
    """
    Função que retorna a tela de login.
    """
    return ft.View(
        "/login",
        [
            ft.Text('Login', size=30, weight="bold"),

            # Campo de email
            ft.TextField(
                label="Informe seu email", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
                color="Blue",
            ),

            # Campo de senha com ícone
            senha_row,

            # Botão de entrar redirecionando para /tela_inicial
            ft.ElevatedButton("Entrar", on_click=lambda _: page.go("/tela_inicial")),

            # Botão de cadastro
            ft.ElevatedButton("Não possui cadastro?", on_click=lambda _: page.go("/tela_cadastro")),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

def tela_cadastro(page, senha_row, senha_confirmar_row):
    """
    Função que retorna a tela de cadastro.
    """
    return ft.View(
        "/tela_cadastro", [
            ft.Text("Tela de Cadastro", size=30, weight="bold"),

            # Campo de nome completo
            ft.TextField(
                label="Informe seu nome completo", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
            ),

            # Campo de email
            ft.TextField(
                label="Informe seu email", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
                color="Blue",
            ),

            # Campos de senha e confirmação de senha
            senha_row,
            senha_confirmar_row,

            # Botão de cadastrar
            ft.ElevatedButton("Cadastrar", on_click=lambda _: page.go("/tela_inicial")),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

def tela_inicial(evento):
    """
    Função que retorna a tela inicial
    """
    return ft.View()

def tela_usuario(e):
    pass

def tela_agenda(e):
    pass





