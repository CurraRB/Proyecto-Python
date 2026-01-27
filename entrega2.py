import json
import logging

# Configuración básica del logging
logging.basicConfig(filename='biblioteca.log', level=logging.INFO)

# Diccionario de libros
libros = {}

def cargar_libros():
    """Carga libros desde JSON"""
    global libros
    try:
        with open('libros.json', 'r') as archivo:
            libros = json.load(archivo)
        logging.info("Libros cargados")
    except:
        libros = {}
        logging.info("Archivo no encontrado, iniciando vacío")

def guardar_libros():
    """Guarda libros en JSON"""
    with open('libros.json', 'w') as archivo:
        json.dump(libros, archivo, indent=4)
    logging.info("Libros guardados")

def insertar_elemento():
    """Inserta un nuevo elemento en la biblioteca"""
    titulo = input("Introduce el título del libro: ")
    while not titulo:
        print("El título no puede estar vacío.")
        titulo = input("Introduce el título del libro: ")

    autor = input("Introduce el autor del libro: ")
    while not autor:
        print("El autor no puede estar vacío.")
        autor = input("Introduce el autor del libro: ")

    ano = input("Introduce el año de publicación: ")
    while not ano.isdigit(): 
        ano = input("Introduce el año de publicación: ")

    libros[titulo] = {'autor': autor, 'año': int(ano)}
    guardar_libros()  # Guardamos después de añadir
    logging.info(f"Libro añadido: {titulo}")
    print("Libro '" + titulo + "' añadido con éxito.")

def buscar_elemento():
    """Busca un libro por su título"""
    titulo = input("Introduce el título del libro a buscar: ")
    if titulo in libros:
        print("Libro encontrado: " + str(libros[titulo]))
        logging.info(f"Libro encontrado: {titulo}")
    else:
        print("Libro no encontrado.")
        logging.info(f"Libro no encontrado: {titulo}")

def modificar_elemento():
    """Modifica los datos de un libro creado anteriormente."""
    titulo = input("Introduce el título del libro a modificar: ")
    if titulo in libros:
        autor = input("Introduce el nuevo autor de '" + titulo + "': ")
        while not autor:
            print("El autor no puede estar vacío.")
            autor = input("Introduce el nuevo autor de '" + titulo + "': ")
        
        ano = input("Introduce el nuevo año de publicación de '" + titulo + "': ")
        while not ano.isdigit():
            ano = input("Introduce el nuevo año de publicación de '" + titulo + "': ")

        libros[titulo] = {'autor': autor, 'año': int(ano)}
        guardar_libros()  # Guardamos después de modificar
        logging.info(f"Libro modificado: {titulo}")
        print("Datos de '" + titulo + "' modificados con éxito.")
    else:
        print("Libro no encontrado.")

def eliminar_elemento():
    """Elimina un libro de la biblioteca"""
    titulo = input("Introduce el título del libro a eliminar: ")
    try:
        del libros[titulo]
        guardar_libros()  # Guardamos después de eliminar
        logging.info(f"Libro eliminado: {titulo}")
        print("Libro '" + titulo + "' eliminado con éxito.")
    except KeyError:
        print("El libro no existe.")

def mostrar_todos():
    """Muestra todos los libros de la biblioteca"""
    if libros:
        print("Libros registrados:")
        for titulo, info in libros.items():
            print("Título: " + titulo + ", Autor: " + info['autor'] + ", Año: " + str(info['año']))
        logging.info("Lista mostrada")
    else:
        print("No hay libros registrados.")

def mostrar_menu():
    """Muestra el menú"""
    cargar_libros()  # Cargamos al inicio
    
    while True:
        print("\nMenú de opciones:")
        print("1. Añadir libro")
        print("2. Buscar libro")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Mostrar todos")
        print("6. Salir")

        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                insertar_elemento()
            elif opcion == 2:
                buscar_elemento()
            elif opcion == 3:
                modificar_elemento()
            elif opcion == 4:
                eliminar_elemento()
            elif opcion == 5:
                mostrar_todos()
            elif opcion == 6:
                print("Saliendo del programa...")
                logging.info("Programa finalizado")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

"""Ejecutar el menú"""
mostrar_menu()
