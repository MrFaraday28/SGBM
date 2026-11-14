"""Acceso a datos del módulo Facultad. Único lugar con SQL de este módulo."""

from sgbm.core.db import conexion
from sgbm.modulos.facultad.modelo import Facultad


def listar(solo_activas: bool = True) -> list[Facultad]:
    sql = "SELECT id, nombre, sigla, activo FROM facultad"
    if solo_activas:
        sql += " WHERE activo"
    sql += " ORDER BY nombre"
    with conexion() as conn:
        return [Facultad(**fila) for fila in conn.execute(sql).fetchall()]


def existe_sigla(sigla: str, excluir_id: int | None = None) -> bool:
    sql = "SELECT 1 FROM facultad WHERE upper(sigla) = upper(%s) AND id IS DISTINCT FROM %s"
    with conexion() as conn:
        return conn.execute(sql, (sigla, excluir_id)).fetchone() is not None


def insertar(f: Facultad) -> int:
    sql = "INSERT INTO facultad (nombre, sigla, activo) VALUES (%s, %s, %s) RETURNING id"
    with conexion() as conn:
        return conn.execute(sql, (f.nombre, f.sigla, f.activo)).fetchone()["id"]


def actualizar(f: Facultad) -> None:
    sql = "UPDATE facultad SET nombre = %s, sigla = %s, activo = %s WHERE id = %s"
    with conexion() as conn:
        conn.execute(sql, (f.nombre, f.sigla, f.activo, f.id))


def dar_de_baja(facultad_id: int) -> None:
    """Baja lógica: las materias y bibliografías históricas siguen referenciándola."""
    with conexion() as conn:
        conn.execute("UPDATE facultad SET activo = false WHERE id = %s", (facultad_id,))
