# ADR 0002 — Entregables formales en Word, documentación viva en Markdown

**Estado:** Propuesto
**Fecha:** 2026-11-14

## Contexto

El Acta (sección VI) fija Microsoft Word vía M365 para la documentación. Los archivos `.docx` son binarios: en
git no muestran diferencias, no se pueden fusionar y generan conflictos cuando dos personas editan a la vez.

## Decisión

- Entregables de la cátedra (Acta, Plan de Gestión, EDT, cronograma, RACI, Informe de Cierre): se editan en Word/Excel
  en OneDrive/Teams. Al aprobarse una versión, se exporta a PDF y se sube a `docs/<grupo-proceso>/`.
- Documentación técnica y de Sprint: Markdown dentro del repo, revisada en el mismo PR que el código.
- `.docx` y `.doc` están en `.gitignore`.

## Consecuencias

- Se respeta lo comprometido en el Acta (Word sigue siendo la herramienta de documentación formal).
- El repo tiene un historial legible y auditable de cada decisión técnica.
