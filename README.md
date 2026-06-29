# TPI-Programación1-Lopez-Antonella

## TPI: Sistema de Gestión de Países

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Descripción

Aplicación de consola en Python 3 que gestiona un dataset de países del mundo. Lee y escribe datos desde un archivo CSV y ofrece un menú interactivo para agregar, actualizar, buscar, filtrar, ordenar y calcular estadísticas. El CSV se crea automáticamente si no existe.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Estructura del proyecto

tpi-gestion-paises/
├── paises.py        ← Código fuente principal
├── paises.csv       ← Dataset (se genera automáticamente)
└── README.md        ← Este archivo

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Cómo ejecutar


Tener Python 3 instalado.
Colocar paises.py en una carpeta.
Abrir terminal en esa carpeta y ejecutar:


bashpython paises.py

El archivo paises.csv se crea solo en la misma carpeta la primera vez que se ejecuta el programa.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Opciones del menú

OpciónDescripción1Mostrar todos los países2Agregar un nuevo país3Actualizar población o superficie4Buscar país por nombre (parcial o exacto)5Filtrar por continente, rango de población o superficie6Ordenar por nombre, población o superficie (asc/desc) — guarda en CSV7Ver estadísticas generales0Salir

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejemplos de uso

Agregar un país

Elegí una opcion: 2
-- AGREGAR PAIS --
  Nombre: Italia
  Poblacion: 60317000
  Superficie en km2: 301340
  Continente: Europa
  [OK] Pais 'Italia' agregado.

Buscar por nombre parcial

Elegí una opcion: 4
  Nombre o parte del nombre: arg
  Se encontraron 1 resultado(s):
  N°   Nombre          Poblacion   Superficie km2  Continente
  1    Argentina      45,376,763        2,780,400  America

Filtrar por continente

Elegí una opcion: 5  ->  1
  Continente: Europa
  (Muestra Alemania, Francia, Espana)

Ordenar y guardar en CSV

Elegí una opcion: 6  ->  2 (Poblacion)  ->  2 (Descendente)
  [OK] Datos guardados en 'paises.csv'.
  Paises ordenados por poblacion (descendente): ...

Estadísticas

Elegí una opcion: 7
  Total de paises: 8
  Mayor poblacion : Estados Unidos (331893745 hab.)
  Menor poblacion : Canada (41500000 hab.)
  Promedio de poblacion  : 122637221 hab.
  Promedio de superficie : 4167877 km2
  Paises por continente:
    America: 4
    Europa: 3
