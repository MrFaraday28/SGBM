"""Pantallas Flet del módulo Bibliografías. No importa repositorio ni core.db."""

import flet as ft


def construir(page: ft.Page) -> ft.Control:
    return ft.Column(
        [
            ft.Text("Gestión de Bibliografías", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("En construcción — Incremento 4 (Sprint 4)."),
        ]
    )
