================================================================================
INDEX
- WHERE: 13
- GROUP BY: 1,2,3,4,12
- HAVING: 5,6
- SUBCONSULTAS: 7,8,10,14
- FUNCIONES: 9,11

================================================================================
1. AGRUPAR POR EDAD Y CONTAR CUANTOS CLIENTES HAY EN CADA GRUPO

SELECT edad, COUNT(*) AS CantidadDeClientes
FROM Cliente
GROUP BY edad;

+------+--------------------+
| edad | CantidadDeClientes |
+------+--------------------+
|   25 |                  3 |
|   30 |                  3 |
|   22 |                  1 |
|   35 |                  1 |
|   28 |                  2 |
+------+--------------------+
================================================================================
2. CALCULAR EL INGRSO PROMEDIO POR GRUPO DE EDAD

SELECT edad, AVG(ingresos) AS IngresoPromedio
FROM Cliente
GROUP BY edad;

+------+-----------------+
| edad | IngresoPromedio |
+------+-----------------+
|   25 |    66666.666667 |
|   30 |    55000.000000 |
|   22 |    40000.000000 |
|   35 |    90000.000000 |
|   28 |    67500.000000 |
+------+-----------------+
================================================================================
3. AGRUPAR POR HISTORIAL DE COMPRAS Y OBTENER LA  SUMA TOTAL DE INGRESOS EN CADA
   GRUPO. ORDENADO DE MANERA ASCENDENTE POR EL TOTAL DE INGRESOS.

SELECT historial_compras, SUM(ingresos) AS TotalIngresos
FROM Cliente
GROUP BY historial_compras
ORDER BY TotalIngresos ASC;

+-------------------+---------------+
| historial_compras | TotalIngresos |
+-------------------+---------------+
|                 3 |      50000.00 |
|                 1 |      60000.00 |
|                 5 |     125000.00 |
|                 7 |     180000.00 |
|                 2 |     215000.00 |
+-------------------+---------------+
================================================================================
4. AGRUPAR POR RANGOS DE INGRESOS Y CONTAR CUANTOS CLIENTES HAY EN CADA RANGO.

BAJO 50000 MEDIO 80000 ALTO

]INF, 50000[     BAJO
[50000, 80000]   MEDIO
]80000, INF[     ALTO

SELECT
    CASE
        WHEN ingresos < 50000 THEN 'Bajo'
        WHEN ingresos BETWEEN 50000 AND 80000 THEN 'Medio'
        ELSE 'Alto'
    END AS RangoIngresos,
    COUNT(*) AS CantidadDeClientes
FROM Cliente
GROUP BY RangoIngresos;

+---------------+--------------------+
| RangoIngresos | CantidadDeClientes |
+---------------+--------------------+
| Medio         |                  6 |
| Bajo          |                  2 |
| Alto          |                  2 |
+---------------+--------------------+
================================================================================
5. CONTAR EL NUMERO DE CLIENTES POR EDAD, PERO SOLO MOSTRAR GRUPOS  CON  MAS  DE
   UN CLIENTE.
   
SELECT Edad, COUNT(*) AS CantidadDeClientes
FROM Cliente
GROUP BY Edad
HAVING CantidadDeClientes > 1;

+------+--------------------+
| Edad | CantidadDeClientes |
+------+--------------------+
|   25 |                  3 |
|   30 |                  3 |
|   28 |                  2 |
+------+--------------------+
================================================================================
6. CALCULAR EL INGRESO PROMEDIO POR GRUPO DE EDAD, PERO SOLO MOSTRAR GRUPOS  CON
   INGRESO PROMEDIO SUPERIOR A 60000.

SELECT edad, AVG(ingresos) as IngresoPromedio
FROM Cliente
GROUP BY edad
HAVING IngresoPromedio > 60000;

+------+-----------------+
| edad | IngresoPromedio |
+------+-----------------+
|   25 |    66666.666667 |
|   35 |    90000.000000 |
|   28 |    67500.000000 |
+------+-----------------+
================================================================================
7. ENCONTRAR CLIENTES CON INGRESOS MAYORES AL INGRESO PROMEDIO.

SELECT id_cliente nombre, ingresos
FROM Cliente
WHERE Ingresos > (SELECT AVG(ingresos) FROM Cliente);

+--------+----------+
| nombre | ingresos |
+--------+----------+
|      2 | 75000.00 |
|      4 | 90000.00 |
|      7 | 90000.00 |
|      8 | 75000.00 |
+--------+----------+
================================================================================
8. ENCONTRAR CLIENTES CUYA EDAD ESTE POR ENCIMA DEL PROMEDIO DE EDAD DE AQUELLOS
   CON HISTORIAL DE COMPRAS MAYOR A 3.

SELECT id_cliente, nombre, edad
FROM Cliente
WHERE edad > (SELECT AVG(edad) FROM Cliente WHERE historial_compras > 3);

+------------+--------+------+
| id_cliente | nombre | edad |
+------------+--------+------+
|          4 | Ana    |   35 |
+------------+--------+------+
================================================================================
9. CALCULAR LA EDAD PROMEDIO DE LOS CLIENTES.

SELECT AVG(edad) AS EdadPromedio
FROM Cliente;

+--------------+
| EdadPromedio |
+--------------+
|      27.8000 |
+--------------+
================================================================================
10. ENCONTRAR AL CLIENTE CON EL INGRESO MAS ALTO.

SELECT MAX(ingresos) FROM Cliente;

SELECT id_cliente, nombre, ingresos
FROM Cliente
WHERE ingresos = (SELECT MAX(ingresos) FROM Cliente);

+------------+--------+----------+
| id_cliente | nombre | ingresos |
+------------+--------+----------+
|          4 | Ana    | 90000.00 |
|          7 | Ana    | 90000.00 |
+------------+--------+----------+
================================================================================
11. CALCULAR LA SUMA TOTAL DE INGRESOS DE TODOS LOS CLIENTES.

SELECT SUM(ingresos) AS IngresosTotales
FROM Cliente;

+-----------------+
| IngresosTotales |
+-----------------+
|       630000.00 |
+-----------------+
================================================================================
12. CALCULAR EL NUMERO DE CLIENTES EN CADA GRUPO DE EDAD

SELECT edad, COUNT(*) AS CantidadDeClientes
FROM Cliente
GROUP BY edad;

+------+--------------------+
| edad | CantidadDeClientes |
+------+--------------------+
|   25 |                  3 |
|   30 |                  3 |
|   22 |                  1 |
|   35 |                  1 |
|   28 |                  2 |
+------+--------------------+
================================================================================
13. OBTENER EL NOMBRE Y LA EDAD DE LOS CLIENTES CON INGRESOS SUPERIORES  A 60000
    ORDENADOS POR EDAD DE FORMA DESCENDENTE.

SELECT nombre, edad
FROM Cliente
WHERE ingresos > 60000
ORDER BY edad DESC;

+--------+------+
| nombre | edad |
+--------+------+
| Ana    |   35 |
| María  |   30 |
| Ismael |   28 |
| Ana    |   25 |
+--------+------+
================================================================================
14. OBTENER EL NOMBRE DE CADA CLIENTE JUNTO CON LA DIFERENCIA  ENTRE  SU INGRESO
    Y EL INGRESO PROMEDIO DE TODOS LOS CLIENTES.

SELECT 
    nombre,
	ingresos - (SELECT AVG(ingresos) FROM Cliente) AS DiferenciaIngresoPromedio
FROM Cliente;

+--------+---------------------------+
| nombre | DiferenciaIngresoPromedio |
+--------+---------------------------+
| Juan   |             -13000.000000 |
| María  |              12000.000000 |
| Pedro  |             -23000.000000 |
| Ana    |              27000.000000 |
| Luis   |              -3000.000000 |
| Juan   |              -3000.000000 |
| Ana    |              27000.000000 |
| Ismael |              12000.000000 |
| María  |             -23000.000000 |
| Liz    |             -13000.000000 |
+--------+---------------------------+  
================================================================================






