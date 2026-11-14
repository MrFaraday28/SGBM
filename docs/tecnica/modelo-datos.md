# Modelo de datos

Fuente de verdad: `db/migraciones/`. Este documento explica el porqué; si contradice al SQL, manda el SQL.

## Diagrama

```
 facultad 1───* sede
    │  1
    ├───* autoridad
    │  1
    └───* materia 1───* bibliografia *───1 libro *───1 categoria
                                             │
                                             * libro_autor *───1 autor
```

## Tablas

```
 Tabla          Módulo        Propósito
 ─────────────  ────────────  ──────────────────────────────────────────────────────────
 facultad       Facultad      Unidad académica. Baja lógica.
 sede           Facultad      Sedes de cada facultad.
 autoridad      Facultad      Decano, vicedecano, etc. Histórico con flag "vigente".
 materia        Materia       Materia de un plan de estudio, pertenece a una facultad.
 categoria      Libro         Clasificación temática de libros.
 autor          Libro         Autores (N:M con libro).
 libro          Libro         Catálogo bibliográfico (solo metadatos, sin archivos).
 libro_autor    Libro         Relación libro ↔ autor con orden de autoría.
 bibliografia   Bibliografía  Libro asignado a materia por período, Obligatoria/Complementaria.
```

## Decisiones clave

- **Solo metadatos**: no se almacenan archivos digitales (alcance confirmado).
- **Bajas lógicas** en facultad, materia y libro para no romper bibliografías históricas.
- **Período** en `bibliografia`: la misma materia puede cambiar su bibliografía cada semestre sin perder historial.
- **Aprobación** (`aprobado_por`, `aprobado_en`): el Decano aprueba las fuentes (Acta, sección V).
