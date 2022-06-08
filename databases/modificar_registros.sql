-- Sentencia Where, para filtrar
SELECT * FROM Usuario WHERE edad <= 26;

-- Para actualizar un registro se necesita Where
UPDATE Usuario SET edad = 51 WHERE id = 3;

-- Para eliminar un registro se necesita Where
DELETE FROM Usuario WHERE id = 11;