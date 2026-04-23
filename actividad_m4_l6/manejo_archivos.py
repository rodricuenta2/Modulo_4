# manejo_archivos.py

# --- 1. Escribir en un archivo ---
# Usamos 'w' para crear/sobreescribir el archivo
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea 1: Bienvenidos al curso de Python.\n")
    archivo.write("Línea 2: Este es un ejercicio de manejo de archivos.\n")
    archivo.write("Línea 3: Aprendiendo a usar write().\n")

print("--- Archivo creado y escrito con éxito ---\n")


# --- 2. Leer el archivo completo ---
print("--- Contenido completo del archivo (read): ---")
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)


# --- 3. Leer línea por línea ---
print("--- Lectura específica (readline + ciclo for): ---")
with open("datos.txt", "r", encoding="utf-8") as archivo:
    # Leer e imprimir solo la primera línea
    primera_linea = archivo.readline()
    print(f"Primera línea: {primera_linea.strip()}")
    
    # Ciclo for para leer el resto (el puntero ya está en la segunda línea)
    print("Resto del archivo:")
    for linea in archivo:
        print(linea.strip())
print()


# --- 4. Añadir contenido (modo append) ---
# Usamos 'a' para agregar sin borrar lo anterior
with open("datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea 4: Esta línea fue añadida con el modo append.\n")

# Comprobación de la lectura
print("--- Comprobación tras el append: ---")
with open("datos.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())


# --- 5. Atributos y cierre ---
# Abrimos el archivo para mostrar sus atributos
archivo_final = open("datos.txt", "r", encoding="utf-8")

print("--- Atributos del archivo: ---")
print(f"Nombre del archivo: {archivo_final.name}")
print(f"Modo de apertura: {archivo_final.mode}")
print(f"¿Está el archivo cerrado?: {archivo_final.closed}")

# Cerramos el archivo manualmente
archivo_final.close()

print(f"¿Está el archivo cerrado ahora?: {archivo_final.closed}")