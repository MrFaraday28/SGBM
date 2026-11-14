"""Pantallas Flet del módulo Facultad. No importa repositorio ni core.db."""

import flet as ft

from sgbm.modulos.facultad import servicio
from sgbm.modulos.facultad.modelo import Facultad


def construir(page: ft.Page) -> ft.Control:
    nombre = ft.TextField(label="Nombre", expand=True)
    sigla = ft.TextField(label="Sigla", width=140)
    tabla = ft.DataTable(
        columns=[ft.DataColumn(ft.Text("Sigla")), ft.DataColumn(ft.Text("Nombre"))], rows=[]
    )

    def avisar(texto: str) -> None:
        page.show_dialog(ft.SnackBar(ft.Text(texto)))  # Flet 0.86: page.open() ya no existe

    def refrescar(actualizar: bool = True) -> None:
        try:
            tabla.rows = [
                ft.DataRow(cells=[ft.DataCell(ft.Text(f.sigla)), ft.DataCell(ft.Text(f.nombre))])
                for f in servicio.listar()
            ]
        except Exception as exc:  # BD no disponible: la pantalla igual se muestra
            avisar(f"No se pudo leer la base de datos: {exc}")
        if actualizar:
            page.update()

    def guardar(_e) -> None:
        try:
            servicio.guardar(Facultad(nombre=nombre.value or "", sigla=sigla.value or ""))
            nombre.value = sigla.value = ""
            avisar("Facultad guardada.")
            refrescar()
        except servicio.ErrorValidacion as exc:
            avisar(str(exc))

    vista = ft.Column(
        [
            ft.Text("Gestión de Facultades", size=22, weight=ft.FontWeight.BOLD),
            ft.Row([nombre, sigla, ft.FilledButton("Guardar", on_click=guardar)]),
            ft.Divider(),
            tabla,
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )
    refrescar(actualizar=False)  # main.py hace page.update() al montar la vista
    return vista
