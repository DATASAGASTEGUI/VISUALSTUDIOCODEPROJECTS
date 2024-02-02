-- 1. CREAR UNA TABLA 

DROP TABLE IF EXISTS Alumno;

CREATE TABLE Alumno (
   idAlumno         INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
   nombre           VARCHAR(20) NOT NULL,
   nota             INTEGER     NOT NULL,
   estatura         DOUBLE      NOT NULL,
   fecha_nacimiento VARCHAR(10) NOT NULL,
   casado           BOOLEAN     NOT NULL
);
  
-- 2. MOSTRAR LAS TABLAS DE UNA BASE DE DATOS 

SELECT * FROM sqlite_master WHERE type = "table";

-- 3. MOSTRAR LA ESTRUCTURA DE UNA TABLA

PRAGMA table_info(Alumno);

-- 4. INSERTAR REGISTROS A UNA TABLA

INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Carlos',5,1.70,'2000-01-15',true);
INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Miguel',10,1.65,'1999-02-20',false);
INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('María',7,1.60,'2000-04-10',true);
INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('José',8,1.65,'2005-03-23',false);
INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Alicia',6,1.72,'1972-01-10',true);
INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Angel',7,1.71,'2000-01-10',true);

-- 5. MOSTRAR TODOS LOS REGISTROS DE UNA TABLA 

SELECT * FROM Alumno;




CREATE TABLE Asignatura (
   idAsignatura     INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
   nombre           VARCHAR(20) NOT NULL,
);