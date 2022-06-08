-- Insertar datos en la base
INSERT INTO Usuario (email, username)
  -VALUES('yanita@mixito.luv','Yanita');

-- Eliminar un registro sin id (Llave primaria)
DELETE FROM Usuario WHERE email = 'danito@mixito.luv' LIMIT 1;

-- Agregar una columna como llave primaria
ALTER TABLE Usuario ADD PRIMARY KEY (id);

-- Indicar id como autoincrementable
ALTER TABLE Usuario MODIFY COLUMN id INT AUTO_INCREMENT;