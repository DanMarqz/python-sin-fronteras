-- Crear una nueva columna
ALTER TABLE Usuario ADD edad int;

-- Eliminar una columna
ALTER TABLE Usuario DROP COLUMN edad;

-- Modificar una columna
ALTER TABLE Usuario MODIFY COLUMN email varchar(50);