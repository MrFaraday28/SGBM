-- ════════════════════════════════════════════════════════════════════
-- SGBM · V001 · Esquema inicial (propuesta v0 — validar en Sprint 1)
-- Regla: este archivo NO se edita una vez en main. Cambios → V002, V003...
-- ════════════════════════════════════════════════════════════════════

BEGIN;

-- ── Módulo 1: Facultad ──────────────────────────────────────────────
CREATE TABLE facultad (
    id        integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre    varchar(150) NOT NULL,
    sigla     varchar(10)  NOT NULL,
    activo    boolean      NOT NULL DEFAULT true,
    creado_en timestamptz  NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX ux_facultad_sigla ON facultad (upper(sigla));

CREATE TABLE sede (
    id          integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    facultad_id integer      NOT NULL REFERENCES facultad (id),
    nombre      varchar(150) NOT NULL,
    direccion   varchar(250),
    UNIQUE (facultad_id, nombre)
);

CREATE TABLE autoridad (
    id              integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    facultad_id     integer      NOT NULL REFERENCES facultad (id),
    cargo           varchar(80)  NOT NULL,
    nombre_completo varchar(150) NOT NULL,
    vigente         boolean      NOT NULL DEFAULT true
);

-- ── Módulo 2: Materia ───────────────────────────────────────────────
CREATE TABLE materia (
    id             integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    facultad_id    integer      NOT NULL REFERENCES facultad (id),
    codigo         varchar(20)  NOT NULL,          -- p. ej. INFO-300
    nombre         varchar(150) NOT NULL,
    carrera        varchar(150) NOT NULL,
    plan_estudio   varchar(20)  NOT NULL,          -- p. ej. 2020
    semestre       smallint     CHECK (semestre BETWEEN 1 AND 12),
    activo         boolean      NOT NULL DEFAULT true,
    UNIQUE (codigo, plan_estudio)
);
CREATE INDEX ix_materia_facultad ON materia (facultad_id);

-- ── Módulo 3: Libro (catálogo + categoría temática) ─────────────────
-- Decisión de alcance: este módulo NO vincula libros con materias.
-- Ese vínculo pertenece al Módulo 4. Ver docs/tecnica/adr/0003.
CREATE TABLE categoria (
    id     integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre varchar(100) NOT NULL UNIQUE
);

CREATE TABLE autor (
    id              integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_completo varchar(150) NOT NULL
);

CREATE TABLE libro (
    id           integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    isbn         varchar(17)  UNIQUE,              -- nullable: material sin ISBN
    titulo       varchar(300) NOT NULL,
    editorial    varchar(150),
    edicion      varchar(30),
    anio         smallint     CHECK (anio BETWEEN 1450 AND 2100),
    categoria_id integer      REFERENCES categoria (id),
    activo       boolean      NOT NULL DEFAULT true
);
CREATE INDEX ix_libro_titulo ON libro (lower(titulo));

CREATE TABLE libro_autor (
    libro_id integer  NOT NULL REFERENCES libro (id) ON DELETE CASCADE,
    autor_id integer  NOT NULL REFERENCES autor (id),
    orden    smallint NOT NULL DEFAULT 1,
    PRIMARY KEY (libro_id, autor_id)
);

-- ── Módulo 4: Bibliografía (materia ↔ libro) ────────────────────────
CREATE TYPE tipo_bibliografia AS ENUM ('OBLIGATORIA', 'COMPLEMENTARIA');

CREATE TABLE bibliografia (
    id            integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    materia_id    integer           NOT NULL REFERENCES materia (id),
    libro_id      integer           NOT NULL REFERENCES libro (id),
    tipo          tipo_bibliografia NOT NULL,
    periodo       varchar(20)       NOT NULL,      -- p. ej. 2026-Primavera
    aprobado_por  varchar(150),                    -- Decano (ver Acta, sección V)
    aprobado_en   date,
    observacion   varchar(300),
    UNIQUE (materia_id, libro_id, periodo)
);
CREATE INDEX ix_bibliografia_materia ON bibliografia (materia_id, periodo);

COMMIT;
