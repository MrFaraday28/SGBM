# Control Integrado de Cambios

Responde al riesgo R01 del Acta (cambios en los requerimientos).

## Flujo

```
 Interesado pide algo nuevo
        │
        ▼
 Issue "Solicitud de cambio" (plantilla en GitHub)   label: cambio:pendiente
        │
        ▼
 Análisis de impacto (alcance, horas, módulo, Sprint afectado)
        │
        ▼
 Decisión del Líder de Proyecto con el interesado
        │
   ┌────┴─────────┬─────────────────┐
   ▼              ▼                 ▼
 Aprobado       Diferido          Rechazado
 → Product      → Backlog para    → Se cierra con
   Backlog        post-proyecto     justificación
```

Regla: **un cambio aprobado nunca entra al Sprint en curso**, va al siguiente Sprint Planning.

El historial de decisiones queda en los issues con label `cambio:*`; no hace falta duplicarlo acá.
Al cierre del proyecto se exporta la lista al Informe de Cierre.
