"""Reglas de negocio del módulo Facultad. Las vistas solo llaman a este módulo."""

from sgbm.modulos.facultad import repositorio as repo
from sgbm.modulos.facultad.modelo import Facultad


class ErrorValidacion(ValueError):
    """Error de negocio que la vista muestra al usuario tal cual."""


def validar(f: Facultad, existe_sigla=repo.existe_sigla) -> None:
    if not f.nombre or not f.nombre.strip():
        raise ErrorValidacion("El nombre de la facultad es obligatorio.")
    if not f.sigla or not f.sigla.strip():
        raise ErrorValidacion("La sigla es obligatoria.")
    if len(f.sigla.strip()) > 10:
        raise ErrorValidacion("La sigla no puede superar 10 caracteres.")
    if existe_sigla(f.sigla.strip(), f.id):
        raise ErrorValidacion(f"Ya existe una facultad con la sigla {f.sigla.strip().upper()}.")


def guardar(f: Facultad) -> Facultad:
    f.nombre = f.nombre.strip()
    f.sigla = f.sigla.strip().upper()
    validar(f)
    if f.id is None:
        f.id = repo.insertar(f)
    else:
        repo.actualizar(f)
    return f


def listar() -> list[Facultad]:
    return repo.listar()


def dar_de_baja(facultad_id: int) -> None:
    repo.dar_de_baja(facultad_id)
