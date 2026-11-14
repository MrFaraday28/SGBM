# SGBM — Sistema de Gestión de Bibliografías de Materias

Proyecto de la cátedra **INFO-300 Gestión de Proyectos Informáticos** (UAA, Curso 318, Primavera 2026).

Aplicación de escritorio para gestionar la bibliografía de las materias, organizada por facultad y materia.

## Módulos (entregables incrementales)

```
 Incremento  Módulo         Paquete                         Alcance
 ──────────  ─────────────  ──────────────────────────────  ─────────────────────────────────────
 1           Facultad       src/sgbm/modulos/facultad       Facultades, sedes, autoridades
 2           Materia        src/sgbm/modulos/materia        ABM de materias + vínculo a facultad
 3           Libro          src/sgbm/modulos/libro          Catálogo de libros + categorías
 4           Bibliografía   src/sgbm/modulos/bibliografia   Materia ↔ libro (oblig./compl.) + reportes
```

## Stack

```
 Lenguaje          Python 3.14.7
 Base de datos     PostgreSQL 18.6
 Interfaz          Flet 0.86.4 (modo escritorio)
 IDE               Visual Studio Code
 Versionado        Git + GitHub
 Docs formales     Microsoft Word (M365) → PDF versionado en docs/
```

## Puesta en marcha

```bash
git clone https://github.com/<organizacion>/sgbm.git
cd sgbm
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env          # completar credenciales locales
psql -U postgres -c "CREATE DATABASE sgbm;"
psql -U postgres -d sgbm -f db/migraciones/V001__esquema_inicial.sql
psql -U postgres -d sgbm -f db/seeds/datos_prueba.sql
python -m sgbm.main
```

## Estructura del repositorio

```
sgbm/
├── src/sgbm/
│   ├── main.py               Punto de entrada Flet (navegación entre módulos)
│   ├── config.py             Lectura de variables de entorno
│   ├── core/db.py            Pool de conexiones PostgreSQL
│   └── modulos/<modulo>/     Un paquete por módulo, mismas 4 capas:
│       ├── modelo.py           Entidades (dataclasses)
│       ├── repositorio.py      SQL (único lugar que toca la BD)
│       ├── servicio.py         Reglas de negocio y validaciones
│       └── vista.py            Pantallas Flet (solo llama al servicio)
├── db/
│   ├── migraciones/          Scripts SQL numerados, nunca se editan una vez aplicados
│   └── seeds/                Datos de prueba
├── tests/                    Pruebas por módulo (pytest)
├── docs/                     Documentación PMBOK + Scrum + técnica (ver docs/README.md)
├── .github/                  Plantillas de issues/PR, CODEOWNERS, CI
└── scripts/                  Automatizaciones (bootstrap de GitHub)
```

## Cómo trabajamos

- Metodología: PMBOK (dirección) + Incremental (producto) + Scrum (ejecución).
- Cada Sprint entrega **un módulo funcional**; la Sprint Review es la **Reunión de Monitoreo y Control**.
- Flujo de ramas, Definición de Hecho y convenciones: [CONTRIBUTING.md](CONTRIBUTING.md).
- Tablero: GitHub Projects (pestaña *Projects* del repositorio).

## Equipo

Alejandro Alegre · Fany Barreto · Mathias Leguizamón · Robert Méndez · Sofía Navarro · Marco Quintana

Interesados: Ms. Juan de Dios Garbett (Decano) · Ms. Blanca Duarte de Báez (Vicedecana)
