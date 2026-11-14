# ADR 0001 — Monorepo con capas por módulo

**Estado:** Propuesto
**Fecha:** 2026-11-14

## Contexto

El Acta identifica como riesgo los problemas de integración entre Front-end, Back-end y Base de Datos al final de
cada Sprint. Separar repositorios por capa, o repartir el trabajo estrictamente por capa, hace que ningún módulo
funcione hasta que las tres partes se juntan.

## Decisión

- Un único repositorio con un paquete por módulo (`facultad`, `materia`, `libro`, `bibliografia`).
- Cada paquete tiene las mismas cuatro capas: `modelo`, `repositorio`, `servicio`, `vista`.
- Las Historias de Usuario se implementan de punta a punta (pantalla → BD) por una misma pareja.
- Los roles por capa (Frontend, Backend, Base de Datos) son **dueños del estándar** de su capa y revisores
  obligatorios vía `CODEOWNERS`, no un paso secuencial.

## Consecuencias

- Integración continua en `main` en lugar de integración al cierre del Sprint.
- Cada integrante toca más de una capa: hay que aprender el patrón, pero baja el bus factor (R07).
