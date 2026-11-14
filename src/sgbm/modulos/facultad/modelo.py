"""Entidades del módulo Facultad."""

from dataclasses import dataclass


@dataclass
class Facultad:
    nombre: str
    sigla: str
    activo: bool = True
    id: int | None = None


@dataclass
class Sede:
    facultad_id: int
    nombre: str
    direccion: str | None = None
    id: int | None = None


@dataclass
class Autoridad:
    facultad_id: int
    cargo: str  # p. ej. Decano, Vicedecano, Director de carrera
    nombre_completo: str
    vigente: bool = True
    id: int | None = None
