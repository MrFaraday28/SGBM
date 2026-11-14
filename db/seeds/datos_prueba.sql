-- Datos de prueba para desarrollo local. No usar en producción.
INSERT INTO facultad (nombre, sigla) VALUES
    ('Facultad de Ciencias y Tecnología', 'FCYT'),
    ('Facultad de Ciencias Empresariales', 'FCE');

INSERT INTO sede (facultad_id, nombre) VALUES (1, 'Sede Central');

INSERT INTO materia (facultad_id, codigo, nombre, carrera, plan_estudio, semestre) VALUES
    (1, 'INFO-300', 'Gestión de Proyectos Informáticos', 'Lic. en Ciencias Informáticas', '2020', 6);

INSERT INTO categoria (nombre) VALUES ('Gestión de proyectos'), ('Ingeniería de software');

INSERT INTO libro (titulo, editorial, edicion, categoria_id) VALUES
    ('Guía de los Fundamentos para la Dirección de Proyectos (Guía del PMBOK)', 'PMI', '5ta', 1);

INSERT INTO bibliografia (materia_id, libro_id, tipo, periodo) VALUES
    (1, 1, 'OBLIGATORIA', '2026-Primavera');
