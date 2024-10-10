from flet import *
import flet as ft

def main(page: ft.Page):

    # Função para trocar de rota (navegação entre telas)
    def on_route_change(e):
        page.views.clear()  # Limpa as views para exibir a nova tela

        if page.route == "/login":
            # Tela de Login
            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.Text("Tela de Login", size=30, weight="bold"),
                        ft.TextField(label="Usuário"),
                        ft.TextField(label="Senha", password=True),
                        ft.ElevatedButton("Ir para Dashboard", on_click=lambda _: page.go("/dashboard"))
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )

        elif page.route == "/dashboard":
            # Tela de Dashboard
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        ft.Text("Bem-vindo ao Dashboard", size=30, weight="bold"),
                        ft.ElevatedButton("Voltar para Login", on_click=lambda _: page.go("/login"))
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )

        page.update()  # Atualiza a página com a nova view

    # Define o que acontece quando a rota muda
    page.on_route_change = on_route_change

    # Defina a rota inicial (primeira tela)
    page.go("/login")

ft.app(target=main)
