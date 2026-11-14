# Documentación del proyecto SGBM

La documentación sigue los **Grupos de Procesos del PMBOK** para la dirección del proyecto, y **Scrum** para
la ejecución. Hay dos tipos de documentos y cada uno vive en un lugar distinto:

```
 Tipo                  Ejemplos                               Fuente (se edita en)        En el repo
 ────────────────────  ─────────────────────────────────────  ──────────────────────────  ─────────────────────
 Entregable formal     Acta, Plan de Gestión, EDT, Gantt,     Word/Excel en OneDrive      PDF de cada versión
 (se entrega a la      RACI, Informe de Cierre                (carpeta Teams del grupo)   APROBADA, con versión
 cátedra)                                                                                 en el nombre
 Documento vivo        Actas de Sprint, registro de riesgos,  Markdown en este repo       El .md mismo
 (cambia con el        solicitudes de cambio, arquitectura,
 código)               modelo de datos, ADRs, specs
```

Motivo: un `.docx` en git es binario (no se ven las diferencias, los merges chocan). Word queda para la
edición colaborativa con formato de cátedra; el repo guarda la **foto aprobada** y todo lo técnico.

Convención de nombre para PDFs: `AAAA-MM-DD_<documento>_v<N>.pdf`
Ejemplo: `2026-09-07_acta-constitucion_v1.pdf`

## Mapa PMBOK → carpetas

```
 Grupo de procesos       Carpeta                         Contenido
 ──────────────────────  ──────────────────────────────  ─────────────────────────────────────────────
 Inicio                  01-inicio/                      Acta de Constitución, registro de interesados
 Planificación           02-planificacion/               Plan de Gestión, EDT, cronograma (.gan + PDF),
                                                         matriz RACI, registro de riesgos
 Ejecución               03-ejecucion/sprints/           Sprint Planning, Sprint Backlog, retrospectiva
 Monitoreo y Control     03-ejecucion/sprints/ (actas)   Acta de Reunión de Monitoreo y Control
                         04-control-cambios/             Solicitudes de cambio y su decisión
 Cierre                  05-cierre/                      Informe de Cierre, lecciones aprendidas
 (Técnico)               tecnica/                        Arquitectura, modelo de datos, ADRs, módulos,
                                                         manual de usuario
```

## Trazabilidad (lo que la cátedra va a querer ver)

```
 EDT (paquete de trabajo)  →  Epic en GitHub (1 por módulo)      label: modulo:<x>
       ↓
 Historia de Usuario       →  Issue con plantilla "Historia"    milestone: Sprint N
       ↓
 Código                    →  Pull Request "Cierra #<issue>"
       ↓
 Incremento                →  Release/Tag vN.0.0
       ↓
 Validación interesados    →  docs/03-ejecucion/sprints/sprint-0N/acta-monitoreo-control.md
```
