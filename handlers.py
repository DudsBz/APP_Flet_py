from flet import *
import flet as ft

# handlers.py

def alternar_visibilidade_senha(e, txt_senha, icon_eye, page):
    """
    Alterna a visibilidade da senha.
    """
    txt_senha.password = not txt_senha.password  # Alterna a visibilidade da senha
    icon_eye.icon = ft.icons.VISIBILITY if txt_senha.password else ft.icons.VISIBILITY_OFF  # Altera o ícone
    page.update()  # Atualiza a página para refletir a mudança
