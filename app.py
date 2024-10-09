from flet import *
import flet as ft

def main(page: ft.Page):
    
    

    def on_route_change (e):
        page.views.clear()
        if page.route == "/login":
            # Definindo o título da página
            page.title = "PrepWise"

            # Tela de Login
            page.views.append(
            ft.View(
                "/login",
                [
                    ft.Text('Login', size=30, weight="bold"),

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
                    # Campo de senha
                    ft.TextField(
                        label="Informe sua senha", 
                        text_align=ft.TextAlign.LEFT,
                        text_style=ft.TextStyle(size=15, weight="bold"),
                        width=270,  # Ligeiramente menor para encaixar o ícone
                        border_radius=10,
                        max_length=30,
                        password=True,  # Esconder a senha por padrão
                    ),

                    # Botão de entrar
                    ft.ElevatedButton("Entrar", on_click=lambda _: page.go("/tela_inicial")),
                    
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif page.route == "/tela_inicial":
            # Tela de outra_tela
            page.views.append(
                ft.View(
                    "/tela_inicial",
                    [
                        ft.Text("Bem-vindo a tela inicial", size=30, weight="bold"),
                        ft.ElevatedButton("Ir para Login", on_click=lambda _: page.go("/login"))
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )   
        page.update()  # Atualiza a página com a nova view
    
    page.on_route_change = on_route_change

    # Defina a rota inicial (primeira tela)
    page.go("/login")

ft.app(target=main)
