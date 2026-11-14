# Registro de Riesgos

Documento vivo. Se revisa en cada Sprint Planning y en cada Reunión de Monitoreo y Control.
Escala: Probabilidad (P) e Impacto (I) de 1 a 3. Exposición = P × I.

```
 ID   Riesgo                                   Origen   P  I  Exp  Respuesta     Dueño        Estado
 ───  ───────────────────────────────────────  ───────  ─  ─  ───  ────────────  ───────────  ───────
 R01  Cambios en los requerimientos            Acta     3  2   6   Mitigar       Líder        Abierto
 R02  Problemas de integración Front/Back/BD   Acta     2  3   6   Mitigar       Coordinador  Abierto
 R03  Falta de disponibilidad del equipo       Acta     3  2   6   Mitigar       Líder        Abierto
 R04  Solapamiento de alcance Módulo 3 vs 4    Nuevo    3  2   6   Evitar        Líder        Abierto
 R05  Cambios de API en Flet (pre-1.0)         Nuevo    2  2   4   Mitigar       Frontend     Abierto
 R06  Credenciales de BD en cada PC cliente    Nuevo    2  3   6   Mitigar       Base Datos   Abierto
 R07  Conocimiento concentrado en 1 persona    Nuevo    2  3   6   Mitigar       Coordinador  Abierto
      por capa (bus factor)
```

## Plan de respuesta

**R01 — Cambios en requerimientos.** Todo pedido nuevo entra como issue *Solicitud de cambio*, nunca al Sprint
en curso. Se evalúa impacto en alcance/tiempo y lo decide el Líder con los interesados. Ver `04-control-cambios/`.

**R02 — Integración.** Cada HU se desarrolla de punta a punta (pantalla → servicio → BD) por la misma pareja.
CI corre en cada PR. Integración continua en `main`, no al final del Sprint.

**R03 — Disponibilidad.** Las fechas de parciales se cargan como hitos bloqueados en el cronograma. Capacidad del
Sprint se calcula descontando semanas de exámenes.

**R04 — Solapamiento Libro/Bibliografía.** Decisión registrada en `tecnica/adr/0003`: Libro = catálogo + categoría;
Bibliografía = vínculo materia↔libro. Validar con la Vicedecana antes del Sprint 3.

**R05 — Flet.** Versión fijada exacta en `pyproject.toml`. Ningún integrante actualiza Flet sin un ADR.

**R06 — Credenciales.** Rol `sgbm_app` sin DELETE ni DDL; `.env` fuera del repo; `.env.example` sin valores reales.

**R07 — Bus factor.** Las revisiones de PR rotan: cada integrante revisa al menos un PR de una capa que no es la suya
por Sprint.
