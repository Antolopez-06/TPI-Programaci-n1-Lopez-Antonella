"""
TPI - Gestión de Datos de Países en Python
Tecnicatura Universitaria en Programación - UTN
Materia: Programación 1
"""

import csv
import os

# ──────────────────────────────────────────────
#  CONSTANTES
# ──────────────────────────────────────────────
# Carpeta donde esta este mismo archivo .py
CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(CARPETA, "paises.csv")
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

# Datos iniciales que se usan para crear el CSV si no existe
DATOS_INICIALES = [
    {"nombre": "Argentina",      "poblacion": 45376763,  "superficie": 2780400, "continente": "America"},
    {"nombre": "Brasil",         "poblacion": 213993437, "superficie": 8515767, "continente": "America"},
    {"nombre": "Mexico",         "poblacion": 130262216, "superficie": 1964375, "continente": "America"},
    {"nombre": "Estados Unidos", "poblacion": 331893745, "superficie": 9833517, "continente": "America"},
    {"nombre": "Alemania",       "poblacion": 83149300,  "superficie": 357022,  "continente": "Europa"},
    {"nombre": "Francia",        "poblacion": 67391582,  "superficie": 551695,  "continente": "Europa"},
    {"nombre": "Espana",         "poblacion": 47326687,  "superficie": 505990,  "continente": "Europa"},
    {"nombre": "Canada",         "poblacion": 41500000,  "superficie": 9984670, "continente": "America"},
]


# ══════════════════════════════════════════════
#  FUNCIONES DE ARCHIVO
# ══════════════════════════════════════════════

def crear_csv(archivo):
    """Crea el archivo CSV con los datos iniciales."""
    try:
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(DATOS_INICIALES)
        print("[OK] Archivo '" + archivo + "' creado con " + str(len(DATOS_INICIALES)) + " paises.")
    except Exception as e:
        print("[ERROR] No se pudo crear el archivo: " + str(e))


def cargar_paises():
    """
    Lee el CSV y devuelve una lista de diccionarios.
    Si el archivo no existe, lo crea primero.
    """
    # Si no existe el archivo, lo creamos
    if not os.path.exists(ARCHIVO_CSV):
        print("[AVISO] No se encontro '" + ARCHIVO_CSV + "'. Creando archivo nuevo...")
        crear_csv(ARCHIVO_CSV)

    paises = []

    try:
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Verificar que la fila tenga los 4 campos
                if not all(campo in fila for campo in CAMPOS):
                    print("[ERROR] Fila incompleta omitida: " + str(fila))
                    continue
                # Convertir poblacion y superficie a entero
                try:
                    pais = {
                        "nombre":     fila["nombre"].strip(),
                        "poblacion":  int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print("[ERROR] Valores invalidos en fila: " + str(fila))

    except Exception as e:
        print("[ERROR] No se pudo leer el archivo: " + str(e))

    return paises


def guardar_paises(paises):
    """Guarda la lista completa de paises en el CSV."""
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        print("[OK] Datos guardados en '" + ARCHIVO_CSV + "'.")
    except Exception as e:
        print("[ERROR] No se pudo guardar: " + str(e))


# ══════════════════════════════════════════════
#  FUNCION AUXILIAR: mostrar tabla
# ══════════════════════════════════════════════

def mostrar_lista(paises):
    """Imprime los paises en formato de tabla."""
    if not paises:
        print("  (No hay paises para mostrar)")
        return

    print()
    print("  " + "-" * 70)
    print("  {:<4} {:<18} {:>14} {:>16} {:<12}".format(
        "N°", "Nombre", "Poblacion", "Superficie km2", "Continente"))
    print("  " + "-" * 70)

    for i, p in enumerate(paises, start=1):
        print("  {:<4} {:<18} {:>14,} {:>16,} {:<12}".format(
            i,
            p["nombre"],
            p["poblacion"],
            p["superficie"],
            p["continente"]
        ))

    print("  " + "-" * 70)
    print()


# ══════════════════════════════════════════════
#  FUNCIONES PRINCIPALES
# ══════════════════════════════════════════════

def agregar_pais(paises):
    """Pide datos al usuario y agrega un nuevo pais a la lista."""
    print("\n-- AGREGAR PAIS --")

    # Nombre: no puede estar vacio ni repetido
    while True:
        nombre = input("  Nombre: ").strip()
        if nombre == "":
            print("  [ERROR] El nombre no puede estar vacio.")
        elif buscar_indice(paises, nombre) is not None:
            print("  [ERROR] Ya existe un pais con ese nombre.")
        else:
            break

    # Poblacion: entero positivo
    while True:
        entrada = input("  Poblacion: ").strip()
        if entrada == "":
            print("  [ERROR] No puede estar vacio.")
            continue
        try:
            poblacion = int(entrada)
            if poblacion <= 0:
                print("  [ERROR] Debe ser un numero positivo.")
            else:
                break
        except ValueError:
            print("  [ERROR] Ingresa un numero entero valido.")

    # Superficie: entero positivo
    while True:
        entrada = input("  Superficie en km2: ").strip()
        if entrada == "":
            print("  [ERROR] No puede estar vacio.")
            continue
        try:
            superficie = int(entrada)
            if superficie <= 0:
                print("  [ERROR] Debe ser un numero positivo.")
            else:
                break
        except ValueError:
            print("  [ERROR] Ingresa un numero entero valido.")

    # Continente: no puede estar vacio
    while True:
        continente = input("  Continente: ").strip()
        if continente == "":
            print("  [ERROR] El continente no puede estar vacio.")
        else:
            break

    # Agregar a la lista y guardar
    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    guardar_paises(paises)
    print("  [OK] Pais '" + nombre + "' agregado.")


def actualizar_pais(paises):
    """Actualiza la poblacion y/o superficie de un pais existente."""
    print("\n-- ACTUALIZAR PAIS --")

    nombre = input("  Nombre del pais a actualizar: ").strip()
    indice = buscar_indice(paises, nombre)

    if indice is None:
        print("  [ERROR] No se encontro el pais '" + nombre + "'.")
        return

    p = paises[indice]
    print("  Encontrado: " + p["nombre"] +
          " | Poblacion: " + str(p["poblacion"]) +
          " | Superficie: " + str(p["superficie"]))

    # Nueva poblacion (Enter para mantener)
    while True:
        entrada = input("  Nueva poblacion (Enter para no cambiar): ").strip()
        if entrada == "":
            break
        try:
            nueva = int(entrada)
            if nueva <= 0:
                print("  [ERROR] Debe ser un numero positivo.")
            else:
                paises[indice]["poblacion"] = nueva
                break
        except ValueError:
            print("  [ERROR] Ingresa un numero entero valido.")

    # Nueva superficie (Enter para mantener)
    while True:
        entrada = input("  Nueva superficie (Enter para no cambiar): ").strip()
        if entrada == "":
            break
        try:
            nueva = int(entrada)
            if nueva <= 0:
                print("  [ERROR] Debe ser un numero positivo.")
            else:
                paises[indice]["superficie"] = nueva
                break
        except ValueError:
            print("  [ERROR] Ingresa un numero entero valido.")

    guardar_paises(paises)
    print("  [OK] Pais actualizado.")


def buscar_pais(paises):
    """Busca paises cuyo nombre contenga el texto ingresado."""
    print("\n-- BUSCAR PAIS --")

    termino = input("  Nombre o parte del nombre: ").strip()
    if termino == "":
        print("  [ERROR] Ingresa al menos un caracter.")
        return

    resultados = []
    for p in paises:
        if termino.lower() in p["nombre"].lower():
            resultados.append(p)

    if not resultados:
        print("  No se encontraron paises con '" + termino + "'.")
    else:
        print("  Se encontraron " + str(len(resultados)) + " resultado(s):")
        mostrar_lista(resultados)


def buscar_indice(paises, nombre):
    """Devuelve el indice del pais con ese nombre exacto, o None si no existe."""
    for i in range(len(paises)):
        if paises[i]["nombre"].lower() == nombre.lower():
            return i
    return None


def filtrar_paises(paises):
    """Submenú para filtrar paises por distintos criterios."""
    print("\n-- FILTRAR PAISES --")
    print("  1. Por continente")
    print("  2. Por rango de poblacion")
    print("  3. Por rango de superficie")
    opcion = input("  Elegí una opcion: ").strip()

    if opcion == "1":
        continente = input("  Continente: ").strip()
        if continente == "":
            print("  [ERROR] Ingresa un continente.")
            return
        resultado = []
        for p in paises:
            if p["continente"].lower() == continente.lower():
                resultado.append(p)
        print("  Paises en '" + continente + "':")
        mostrar_lista(resultado)

    elif opcion == "2":
        try:
            minimo = int(input("  Poblacion minima: ").strip())
            maximo = int(input("  Poblacion maxima: ").strip())
        except ValueError:
            print("  [ERROR] Ingresa numeros enteros validos.")
            return
        if minimo > maximo:
            print("  [ERROR] El minimo no puede ser mayor que el maximo.")
            return
        resultado = []
        for p in paises:
            if minimo <= p["poblacion"] <= maximo:
                resultado.append(p)
        print("  Paises con poblacion entre " + str(minimo) + " y " + str(maximo) + ":")
        mostrar_lista(resultado)

    elif opcion == "3":
        try:
            minimo = int(input("  Superficie minima (km2): ").strip())
            maximo = int(input("  Superficie maxima (km2): ").strip())
        except ValueError:
            print("  [ERROR] Ingresa numeros enteros validos.")
            return
        if minimo > maximo:
            print("  [ERROR] El minimo no puede ser mayor que el maximo.")
            return
        resultado = []
        for p in paises:
            if minimo <= p["superficie"] <= maximo:
                resultado.append(p)
        print("  Paises con superficie entre " + str(minimo) + " y " + str(maximo) + " km2:")
        mostrar_lista(resultado)

    else:
        print("  [ERROR] Opcion invalida.")


def ordenar_paises(paises):
    """Ordena y muestra la lista segun el criterio elegido."""
    print("\n-- ORDENAR PAISES --")
    print("  Ordenar por:")
    print("  1. Nombre")
    print("  2. Poblacion")
    print("  3. Superficie")
    criterio = input("  Elegí una opcion: ").strip()

    if criterio == "1":
        campo = "nombre"
    elif criterio == "2":
        campo = "poblacion"
    elif criterio == "3":
        campo = "superficie"
    else:
        print("  [ERROR] Opcion invalida.")
        return

    print("  Orden:")
    print("  1. Ascendente")
    print("  2. Descendente")
    orden = input("  Elegí una opcion: ").strip()

    if orden == "1":
        descendente = False
    elif orden == "2":
        descendente = True
    else:
        print("  [ERROR] Opcion invalida.")
        return

    ordenados = sorted(paises, key=lambda p: p[campo], reverse=descendente)

    # Actualizar la lista original y guardar en el CSV
    paises.clear()
    for p in ordenados:
        paises.append(p)
    guardar_paises(paises)

    direccion = "descendente" if descendente else "ascendente"
    print("\n  Paises ordenados por " + campo + " (" + direccion + "):")
    mostrar_lista(paises)


def mostrar_estadisticas(paises):
    """Calcula y muestra estadisticas del dataset."""
    print("\n-- ESTADISTICAS --")

    if not paises:
        print("  No hay datos para calcular.")
        return

    # Mayor y menor poblacion
    mayor = paises[0]
    menor = paises[0]
    for p in paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p

    # Promedios
    total_pob = 0
    total_sup = 0
    for p in paises:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

    prom_pob = total_pob // len(paises)
    prom_sup = total_sup // len(paises)

    # Cantidad por continente
    por_continente = {}
    for p in paises:
        cont = p["continente"]
        if cont in por_continente:
            por_continente[cont] += 1
        else:
            por_continente[cont] = 1

    # Mostrar resultados
    print()
    print("  Total de paises: " + str(len(paises)))
    print()
    print("  Mayor poblacion : " + mayor["nombre"] + " (" + str(mayor["poblacion"]) + " hab.)")
    print("  Menor poblacion : " + menor["nombre"] + " (" + str(menor["poblacion"]) + " hab.)")
    print()
    print("  Promedio de poblacion  : " + str(prom_pob) + " hab.")
    print("  Promedio de superficie : " + str(prom_sup) + " km2")
    print()
    print("  Paises por continente:")
    for cont in por_continente:
        print("    " + cont + ": " + str(por_continente[cont]))
    print()


# ══════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════

def mostrar_menu():
    """Imprime el menu de opciones."""
    print()
    print("=" * 45)
    print("   GESTION DE PAISES - Programacion 1 UTN")
    print("=" * 45)
    print("  1. Mostrar todos los paises")
    print("  2. Agregar un pais")
    print("  3. Actualizar poblacion / superficie")
    print("  4. Buscar pais por nombre")
    print("  5. Filtrar paises")
    print("  6. Ordenar paises")
    print("  7. Ver estadisticas")
    print("  0. Salir")
    print("-" * 45)


def main():
    """Funcion principal: carga los datos y ejecuta el menu."""

    # Cargar (o crear) el CSV al arrancar
    paises = cargar_paises()
    print("  " + str(len(paises)) + " paises cargados.")

    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("  Elegí una opcion: ").strip()

        if opcion == "1":
            mostrar_lista(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n  Hasta luego!\n")
            break
        else:
            print("  [ERROR] Opcion invalida. Elegí un numero del menu.")


# Punto de entrada
if __name__ == "__main__":
    main()
