# Guía de contribución

## 1. Ramas

```
 main                    Siempre funcional. Protegida: solo entra por Pull Request.
 hu/<n>-<descripcion>    Una rama por Historia de Usuario.   Ej: hu/12-alta-facultad
 fix/<n>-<descripcion>   Corrección de un bug reportado.     Ej: fix/31-validar-codigo
 docs/<descripcion>      Solo documentación.                 Ej: docs/acta-sprint-1
```

Reglas:

1. Nadie hace `push` directo a `main`.
2. Cada PR referencia su issue en la descripción (`Cierra #12`) para trazabilidad EDT → HU → código.
3. Mínimo **1 aprobación** de otro integrante; si toca `db/`, aprueba el responsable de Base de Datos (ver `CODEOWNERS`).
4. Merge con **Squash and merge**: un commit por HU en `main`.
5. Ramas de vida corta: si una rama pasa más de 3 días sin merge, se divide la HU.

## 2. Commits

Formato: `<tipo>(<modulo>): <descripcion en presente>`

```
 feat(facultad): alta de sede con validación de nombre único
 fix(materia): corrige filtro por facultad
 db(libro): agrega índice por ISBN
 docs(sprint-1): acta de reunión de monitoreo y control
 test(bibliografia): casos de material obligatorio duplicado
```

Tipos: `feat`, `fix`, `db`, `test`, `docs`, `refactor`, `chore`.

## 3. Base de datos

- Todo cambio de esquema es un **archivo nuevo** en `db/migraciones/` con el siguiente número: `V002__descripcion.sql`.
- **Nunca** se edita una migración que ya está en `main`. Si hay que corregirla, se escribe otra.
- Ninguna vista ni servicio arma SQL: solo `repositorio.py`.

## 4. Capas por módulo (no negociable)

```
 vista.py  ──►  servicio.py  ──►  repositorio.py  ──►  PostgreSQL
 (Flet)         (reglas)          (SQL)
```

Una vista que importa `repositorio` o `core.db` se rechaza en revisión. Esto es lo que mantiene bajo control
el riesgo de integración del Acta.

## 5. Definición de Hecho (DoD)

Una Historia de Usuario está **Hecha** cuando:

- [ ] Cumple todos sus criterios de aceptación.
- [ ] Funciona de punta a punta: pantalla → servicio → BD.
- [ ] Tiene al menos una prueba del servicio en `tests/<modulo>/`.
- [ ] El CI está en verde (lint + tests).
- [ ] Si cambió el esquema, existe la migración y `docs/tecnica/modelo-datos.md` está actualizado.
- [ ] Fue revisada y aprobada en un PR.
- [ ] Está en `main`.

## 6. Cierre de Sprint

1. Todas las HU del milestone `Sprint N` cerradas o devueltas al backlog con justificación.
2. Se crea el tag `vN.0.0` y un *Release* en GitHub con las notas del incremento.
3. Se completa el acta en `docs/03-ejecucion/sprints/sprint-0N/acta-monitoreo-control.md`.
4. Si los interesados piden cambios, **no** se agregan al Sprint: se abre un issue *Solicitud de cambio*
   (ver `docs/04-control-cambios/`).
