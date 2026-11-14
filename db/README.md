# Base de datos

Responsable de estándar: rol **Base de Datos** (ver `CODEOWNERS`).

## Reglas

1. Migraciones numeradas en `migraciones/`: `V001__...sql`, `V002__...sql`. Se aplican en orden.
2. Una migración en `main` es **inmutable**. Corregir = nueva migración.
3. Toda tabla nueva se documenta en `docs/tecnica/modelo-datos.md` en el mismo PR.
4. Bajas siempre **lógicas** (`activo = false`) en facultad, materia y libro: la bibliografía histórica no puede perder referencias.

## Aplicar en local

```bash
for f in db/migraciones/V*.sql; do psql -U postgres -d sgbm -f "$f"; done
psql -U postgres -d sgbm -f db/seeds/datos_prueba.sql
```

## Rol de aplicación (mínimo privilegio)

La app de escritorio se conecta directo a PostgreSQL, así que **cada PC cliente tiene credenciales**.
Por eso la app nunca usa `postgres`:

```sql
CREATE ROLE sgbm_app LOGIN PASSWORD '...';
GRANT CONNECT ON DATABASE sgbm TO sgbm_app;
GRANT USAGE ON SCHEMA public TO sgbm_app;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO sgbm_app;   -- sin DELETE ni DDL
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO sgbm_app;
```
