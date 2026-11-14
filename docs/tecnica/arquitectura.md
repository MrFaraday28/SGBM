# Arquitectura

## Vista general

```
 ┌───────────────────────── PC del usuario (app de escritorio) ─────────────────────────┐
 │                                                                                      │
 │   main.py  (NavigationRail)                                                          │
 │      │                                                                               │
 │      ├── facultad/     vista ─► servicio ─► repositorio ─┐                           │
 │      ├── materia/      vista ─► servicio ─► repositorio ─┤                           │
 │      ├── libro/        vista ─► servicio ─► repositorio ─┼─► core/db.py (pool)       │
 │      └── bibliografia/ vista ─► servicio ─► repositorio ─┘          │                │
 │                                                                     │                │
 └─────────────────────────────────────────────────────────────────────┼────────────────┘
                                                                       │ TCP 5432
                                                          ┌────────────▼────────────┐
                                                          │ PostgreSQL 18 (red UAA) │
                                                          └─────────────────────────┘
```

## Reglas

1. **Monorepo**: un solo repositorio para interfaz, lógica y BD (ADR 0001).
2. **Capas por módulo**: vista → servicio → repositorio. Prohibido saltar capas.
3. **Dependencias entre módulos**: solo a través del `servicio` del otro módulo, nunca de su repositorio.
   Orden permitido: bibliografia → libro, materia → facultad. Nunca al revés.
4. **Errores de negocio**: el servicio lanza `ErrorValidacion`; la vista lo muestra tal cual.

## Decisiones (ADR)

Ver carpeta `adr/`. Cada decisión técnica relevante se registra antes de implementarse.
