-- insertar avistamiento:
INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) VALUES (?, ?, ?, ?, ?, ?)
-- ejemplo: 
--INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) VALUES (130606, '2021-05-03 12:46:11', 'sector alto', 'Observador Perez', 'observador@ejemplo.cl', '+56955555555');

-- insertar detalle_avistamiento:
INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) VALUES (?, ?, ?, ?, ?);
-- ejemplo:
-- INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) VALUES ('2021-04-26 23:46:12', 'insecto', 'muerto', 1);

-- insertar foto:
INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id) VALUES (?, ?, ?);
-- ejemplo:
-- INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id ) VALUES ('/Users/jourzua/personal/DCC/51t/python/archivos/', 'foto-insecto.jpg', 1);

-- seleccionar avistamientos:
SELECT id, comuna_id, dia_hora, sector, nombre, email, celular FROM avistamiento
-- seleccionar ultimos 5 avistamientos ordenados por fecha descendente:
SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo FROM avistamiento AV, detalle_avistamiento DA, comuna CO WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id ORDER BY DA.dia_hora DESC LIMIT 5

-- seleccionar el detalle de un avistamiento
SELECT id, dia_hora, tipo, estado, avistamiento_id FROM detalle_avistamiento WHERE avistamiento_id=?

-- seleccionar información de la fotos de un detalle de avistamiento:
SELECT id, ruta_archivo, nombre_archivo, detalle_avistamiento_id FROM foto WHERE detalle_avistamiento_id=?

