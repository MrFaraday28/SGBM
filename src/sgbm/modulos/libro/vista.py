"""Pantallas Flet del módulo Libros. No importa repositorio ni core.db."""

import flet as ft


def construir(page: ft.Page) -> ft.Control:
    return ft.Column(
        [
            ft.Text("Gestión de Libros", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("En construcción — Incremento 3 (Sprint 3)."),
        ]
    )
