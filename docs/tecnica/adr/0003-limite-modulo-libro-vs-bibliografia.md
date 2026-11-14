# ADR 0003 — Límite entre Módulo 3 (Libro) y Módulo 4 (Bibliografía)

**Estado:** Propuesto — requiere validación de la Vicedecana antes del Sprint 3
**Fecha:** 2026-11-14

## Contexto

El Acta (sección III) describe funciones superpuestas:

- Módulo 3: "la asignación de los libros a sus respectivas materias o categorías se encuentra integrada dentro de este módulo".
- Módulo 4: "crear y administrar el catálogo de recursos bibliográficos, asignar el material de estudio obligatorio
  o complementario a cada materia".

Así redactado, ambos módulos asignan libros a materias y ambos administran un catálogo.

## Decisión

```
 Módulo 3 — Libro          Catálogo de libros (ABM), autores, y asignación a CATEGORÍA temática.
 Módulo 4 — Bibliografía   Asignación libro ↔ MATERIA con tipo Obligatoria/Complementaria por período,
                           aprobación del Decano, y reportes.
```

"Catálogo de recursos bibliográficos" del Módulo 4 se interpreta como la **bibliografía armada por materia**, no
un segundo catálogo de libros.

## Consecuencias

- Una sola tabla de vínculo (`bibliografia`), un solo dueño.
- Si la Vicedecana exige otra cosa, se registra como Solicitud de cambio y se actualiza este ADR.
