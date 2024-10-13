from flet import *
import flet as ft

def main(page: ft.Page):
    
    # Função para alternar a visibilidade da senha
    def icone_visibilidade(e):        
        txt_senha.password = not txt_senha.password  # Alterna a visibilidade da senha
        icon_eye.icon = ft.icons.VISIBILITY if txt_senha.password else ft.icons.VISIBILITY_OFF  # Altera o ícone
        page.update()  # Atualiza a página para refletir a mudança
    def visibilidade_confirm(e):
        txt_confirsenha.password = not txt_confirsenha.password 
        page.update() #para mostrar que isso aconteceu
        

    txt_senha = ft.TextField(
            label="Informe sua senha", 
            text_align=ft.TextAlign.LEFT,
            text_style=ft.TextStyle(size=15, weight="bold"),
            width=260,  # Ligeiramente menor para encaixar o ícone
            border_radius=10,
            max_length=30,
            password=True,  # Esconder a senha por padrão
            )
    txt_confirsenha = ft.TextField(
            label="Informe sua senha", 
            text_align=ft.TextAlign.LEFT,
            text_style=ft.TextStyle(size=15, weight="bold"),
            width=260,  # Ligeiramente menor para encaixar o ícone
            border_radius=10,
            max_length=30,
            password=True,  # Esconder a senha por padrão
            )
        
    icon_eye = ft.IconButton(
            icon=ft.icons.VISIBILITY_OFF,  # Começa com o ícone de olho fechado
            on_click=icone_visibilidade
        )

    # Função para gerenciar as rotas
    def on_route_change(e):
        page.views.clear()  # Limpa as views para adicionar a nova tela

        # Tela de login
        if page.route == "/login":
            # Definindo o título da página
            page.title = "PrepWise"

            # Coloca o campo de senha e o botão de olho na mesma linha
            senha_row = ft.Row(
                controls=[txt_senha, icon_eye],  # Coloca o campo de senha e o ícone na mesma linha   
                alignment=ft.MainAxisAlignment.CENTER
            )

            # Adiciona a view de login à página
            page.views.append(
                ft.View(
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
                        
                        
                        # Adiciona a linha com o campo de senha e o ícone
                        senha_row,

                        # Botão de entrar redirecionando para /tela_inicial
                        ft.ElevatedButton("Entrar", on_click=lambda _: page.go("/tela_inicial")),

                        
                        ft.ElevatedButton("Não possui cadastro?", on_click=lambda _: page.go("/tela_cadastro")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        #Tela Inicial
        elif page.route == "/tela_inicial":
            # Tela inicial
            page.views.append(
                ft.View(
                    "/tela_inicial",
                    [
                        ft.Text("Bem-vindo ao PrepWise", size=30, weight="bold"),

                        ft.ElevatedButton(
                            "Ir para Login", 
                            on_click=lambda _: page.go("/login"),
                        ),
                    ],
                    #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    #vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif page.route == "/tela_cadastro":
            ft.title = "PrepWise - Cadastro"
            senha_row = ft.Row(
                controls=[txt_senha, icon_eye],  # Coloca o campo de senha e o ícone na mesma linha   
                alignment=ft.MainAxisAlignment.CENTER
            )
            senha_confirmar_row = ft.Row(
                controls=[txt_confirsenha],  # Coloca o campo de senha e o ícone na mesma linha   
                alignment=ft.MainAxisAlignment.CENTER
            )
            if txt_confirsenha.value != txt_senha.value:
                msg_erro_campo_senha = ft.Text("Os campos não são compatíveis")
            #tela de cadastro
            page.views.append(
                ft.View(
                    "/tela_cadastro",[
                        ft.Text("Tela de cadastro"),

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
                        
                        # Adiciona a linha com o campo de senha e o ícone
                        senha_row,

                        senha_confirmar_row,
                        
                        msg_erro_campo_senha,

                        # Botão de entrar redirecionando para /tela_inicial
                        ft.ElevatedButton("Cadastrar", on_click=lambda _: page.go("/tela_inicial")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,

                    
                )
            )
        page.update()  # Atualiza a página com a nova view
    
    page.on_route_change = on_route_change

    # Defina a rota inicial (primeira tela)
    page.go("/tela_inicial")

ft.app(target=main)
