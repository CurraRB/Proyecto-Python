libros = {}

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
    print("Libro '" + titulo + "' añadido con éxito.")

def buscar_elemento():
    """Busca un libro por su título"""
    titulo = input("Introduce el título del libro a buscar: ")
    if titulo in libros:
        print("Libro encontrado: " + str(libros[titulo]))
    else:
        print("Libro no encontrado.")

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
        print("Datos de '" + titulo + "' modificados con éxito.")
    else:
        print("Libro no encontrado.")

def eliminar_elemento():
    """Elimina un libro de la biblioteca"""
    titulo = input("Introduce el título del libro a eliminar: ")
    try:
        del libros[titulo]
        print("Libro '" + titulo + "' eliminado con éxito.")
    except KeyError:
        print("El libro no existe.")

def mostrar_todos():
    """Muestra todos los libros de la biblioteca"""
    if libros:
        print("Libros registrados:")
        for titulo, info in libros.items():
            print("Título: " + titulo + ", Autor: " + info['autor'] + ", Año: " + str(info['año']))
    else:
        print("No hay libros registrados.")

def mostrar_menu():
    """Muestra el menú"""
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
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

"""Ejecutar el menú"""
mostrar_menu()
