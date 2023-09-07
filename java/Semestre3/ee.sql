SELECT 
    *
FROM
    estudiantes2022;
INSERT INTO estudiantes2022(idestudiantes2022, nombre, apellido, telefono, email) VALUES('3','Erne','Perez','23452','erne@mail.com');
UPDATE estudiantes2022 SET nombre="ernesto" WHERE idestudiantes2022=3;
ALTER TABLE estudiantes2022 AUTO_INCREMENT=1;
