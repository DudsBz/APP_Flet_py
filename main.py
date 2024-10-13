# main.py
from flet import *
import flet as ft
from components import criar_campo_senha  # Importa o componente
from views import tela_login, tela_cadastro  # Importa as telas
from handlers import alternar_visibilidade_senha  # Importa os manipuladores de eventos

def main(page: ft.Page):
    # Criando os campos de senha e ícones
    txt_senha = ft.TextField(password=True)
    icon_eye = ft.IconButton(icon=ft.icons.VISIBILITY_OFF)

    senha_row = criar_campo_senha("Informe sua senha", txt_senha, lambda e: alternar_visibilidade_senha(e, txt_senha, icon_eye, page))
    senha_confirmar_row = criar_campo_senha("Confirme sua senha", txt_senha, lambda e: alternar_visibilidade_senha(e, txt_senha, icon_eye, page))

    # Função para gerenciar as rotas
    def on_route_change(e):
        page.views.clear()  # Limpa as views para adicionar a nova tela

        if page.route == "/login":
            page.views.append(tela_login(page, senha_row))

        elif page.route == "/tela_cadastro":
            page.views.append(tela_cadastro(page, senha_row, senha_confirmar_row))

        elif page.route == "/tela_inicial":
            page.views.append(
                ft.View(
                    "/tela_inicial",
                    [
                        ft.Text("Bem-vindo ao PrepWise", size=30, weight="bold"),
                        ft.ElevatedButton("Ir para Login", on_click=lambda _: page.go("/login")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = on_route_change
    page.go("/login")  # Rota inicial

ft.app(target=main)
