CREATE DATABASE IF NOT EXISTS  docker;
USE docker ;

CREATE TABLE  vehiculo(
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    matricula varchar(20) NOT NULL,
    id_estado int NOT NULL,
    PRIMARY KEY(matricula)
);

CREATE TABLE  posiciones(
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    latitud float,
    longitud float,
    velocidad int,
    id_vehiculo varchar(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_vehiculo) REFERENCES vehiculo(matricula)
);


INSERT INTO  vehiculo (matricula,id_estado) VALUES ('a123da2',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('f81723d',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('2123d23',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('a2231dz',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('12dwee3',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('123daa1',0);
INSERT INTO  vehiculo (matricula,id_estado) VALUES ('123ad31',0);

INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (142,31,5,'a123da2');
INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (56,185,14,'f81723d');
INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (31,31,129,'2123d23');
INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (123,132,28,'12dwee3');
INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (331,125,1,'123daa1');
INSERT INTO posiciones (latitud,longitud,velocidad,id_vehiculo) VALUES (111,10,153,'123ad31');
