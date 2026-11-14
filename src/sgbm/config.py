"""Configuración leída desde variables de entorno (.env en desarrollo)."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class ConfigDB:
    host: str = os.getenv("SGBM_DB_HOST", "localhost")
    port: int = int(os.getenv("SGBM_DB_PORT", "5432"))
    nombre: str = os.getenv("SGBM_DB_NAME", "sgbm")
    usuario: str = os.getenv("SGBM_DB_USER", "sgbm_app")
    clave: str = os.getenv("SGBM_DB_PASSWORD", "")

    @property
    def dsn(self) -> str:
        return (
            f"host={self.host} port={self.port} dbname={self.nombre} "
            f"user={self.usuario} password={self.clave}"
        )


DB = ConfigDB()
