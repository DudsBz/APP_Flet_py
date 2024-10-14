stack = ft.Stack(
        controls=[
            ft.Container(
                content=ft.Text("Login", size=30, weight="bold"),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.TextField(label="Informe seu nome completo"),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.TextField(label="Informe seu email"),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.TextField(label="Informe sua senha"),
                alignment=ft.alignment.center
            )
        ]
    )
