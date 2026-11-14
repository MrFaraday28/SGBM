"""Pantallas Flet del módulo Materias. No importa repositorio ni core.db."""

import flet as ft


def construir(page: ft.Page) -> ft.Control:
    return ft.Column(
        [
            ft.Text("Gestión de Materias", size=22, weight=ft.FontWeight.BOLD),
            ft.Text("En construcción — Incremento 2 (Sprint 2)."),
        ]
    )
