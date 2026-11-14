"""Pruebas de reglas de negocio de Facultad (sin base de datos)."""

import pytest

from sgbm.modulos.facultad.modelo import Facultad
from sgbm.modulos.facultad.servicio import ErrorValidacion, validar


def sin_duplicados(_sigla, _id):
    return False


def siempre_duplicada(_sigla, _id):
    return True


def test_facultad_valida_no_lanza_error():
    validar(Facultad(nombre="Ciencias y Tecnología", sigla="FCYT"), existe_sigla=sin_duplicados)


@pytest.mark.parametrize("nombre", ["", "   "])
def test_nombre_obligatorio(nombre):
    with pytest.raises(ErrorValidacion, match="nombre"):
        validar(Facultad(nombre=nombre, sigla="FCYT"), existe_sigla=sin_duplicados)


def test_sigla_demasiado_larga():
    with pytest.raises(ErrorValidacion, match="10 caracteres"):
        validar(Facultad(nombre="X", sigla="ABCDEFGHIJK"), existe_sigla=sin_duplicados)


def test_sigla_duplicada():
    with pytest.raises(ErrorValidacion, match="Ya existe"):
        validar(Facultad(nombre="X", sigla="FCYT"), existe_sigla=siempre_duplicada)
