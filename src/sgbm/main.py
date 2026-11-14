"""Punto de entrada de la aplicación de escritorio SGBM."""

import flet as ft

from sgbm.modulos.bibliografia import vista as v_bibliografia
from sgbm.modulos.facultad import vista as v_facultad
from sgbm.modulos.libro import vista as v_libro
from sgbm.modulos.materia import vista as v_materia

MODULOS = [
    ("Facultades", ft.Icons.ACCOUNT_BALANCE, v_facultad.construir),
    ("Materias", ft.Icons.CLASS_, v_materia.construir),
    ("Libros", ft.Icons.MENU_BOOK, v_libro.construir),
    ("Bibliografías", ft.Icons.LIBRARY_BOOKS, v_bibliografia.construir),
]


def main(page: ft.Page) -> None:
    page.title = "SGBM — Gestión de Bibliografías de Materias"
    page.window.min_width = 1000
    page.window.min_height = 650

    contenido = ft.Container(expand=True, padding=20)

    def mostrar(indice: int) -> None:
        contenido.content = MODULOS[indice][2](page)
        page.update()

    menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=icono, label=nombre) for nombre, icono, _ in MODULOS
        ],
        on_change=lambda e: mostrar(e.control.selected_index),
    )

    page.add(ft.Row([menu, ft.VerticalDivider(width=1), contenido], expand=True))
    mostrar(0)


if __name__ == "__main__":
    ft.run(main)
