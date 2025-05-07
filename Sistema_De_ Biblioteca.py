Titulos = {}
ID = 1

# Creamos la función para el listado de libros.
def listadelibros():
    # Nos aseguramos de que hayan libros en la biblioteca.
    if not Titulos:
        print("No hay libros disponibles.")
    else:
        # Se enseña la lista de libros disponibles en la biblioteca.
        for id, libros in Titulos.items():
            print(f"{id} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")

# Creamos la función para agregar un libro.
def agregarlibro():
    # Usamos el global ID para para sumar un entero cada que se añada una clave al diccionario y así tener listas ordenadas.
    global ID
    while True:
        # Global titulos para manegar la lista general de libros.
        global Titulos
        Titulo = input("\nIngrese el titulo del libro:  ")
        Autor = input("Ingrese el autor:  ")
        año = input("Ingrese el año de la obra:  ")
        # Aquí se realizar el proceso de cómo se va a agregar la información al diccionario y la manera en como se agregará.
        Digitos = f"{ID:03d}"
        registro = {"Titulo": Titulo, "Autor":  Autor, "Año": año}
        Titulos[f"ID {Digitos}"] = registro
        ID +=1
        for id, libros in Titulos.items():
            print(f"{id} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")
        # Le damos a escoger al usuario si quiere agregar otro libro, en dado caso que la respuesta sea contraria a "s", terminará el bucle.
        opcion = input("\n¿Desea añadir otro libro? s/n:  ").lower()
        if opcion != 's':
            break

# Creamos la función para buscar un libro.
def buscarlibro():
  # Usamos la lista general de la librería para buscar el libro deseado.
  global Titulos

  while True:
    # Le pedimos la ID al usuario, en este caso pondrá el 001, 002, 003.
    res = (input("\nIngrese la ID del libro que desea buscar (ej:001):  "))
    # Me aseguro de que el valor de la ID sea exactamente al nombre de la clave.
    clave = "ID " + res
    if Titulos:
        # Nos aseguramos que la ID esté en el diccionario, si no está, este mostrará que el libro no ha sido encontrado.
        if clave in Titulos:
            # Creamos la variable donde entramos a la clave y mostramos el contenido de esta.
            libro = Titulos[clave]
            print(f"\n{clave} (Titulo: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Año']})")
            break
        else:
            print("\nLibro no encontrado.")
    else:
        print("\nNo hay libros disponibles.")
        break

def eliminarlibro():
    while True:
        if Titulos:
            # En este caso mostramos los libros disponibles para que el usuario pueda escoger alguno.
            for id, libros in Titulos.items():
                print(f"{id} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")
            res = input("Ingrese la ID del libro que desea eliminar (ej:001):  ")
            clave = "ID " + res
            # Nuevamenete, si el libro esta en el diccionario, procede a borrarlo, en dado caso de que no, pone que el libro no ha sido encontrado.
            if clave in Titulos:
                del Titulos[clave]
                print("El libro se ha eliminado.")
                break
            else:
                print("Libro no encontrado.")
        else:
            print("\nNo hay libros disponibles")
            break

def modificarlibro():
    while True:
        if Titulos:
            try: 
                # Realizamos el mismo proceso de pedir una ID enseñando todos los libros disponibles para decidir cuál editar.
                for id, libros in Titulos.items():
                    print(f"{id} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")
                res = input("\nIngrese la ID del libro que desea modificar (ej:001):  ")
                clave = "ID " + res
                # Si la ID existe, muestra los datos del libro para tener una vista previa para saber qué editar con respecto al libro.
                if clave in Titulos:
                    libros = Titulos[clave]
                    print("Libro actual:")
                    print(f"{clave} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")
                    print("Ingrese los nuevos valores a modificar (Deje en blanco si no modificará algún valor):  ")
                # Pedimos la nueva información ya estando dentro del libro.
                    nuevotitulo = input("Ingrese el nuevo Titulo:  ")
                    nuevoautor = input("Ingrese el nuevo autor:  ")
                    nuevoaño = input("Ingrese el nuevo año:  ")
                # En dado caso de que se agregue nueva información, esta se editará en respecto a la clave, en dado caso de que no, seguirá igual.
                    if nuevotitulo:
                        libros['Titulo'] = nuevotitulo
                    if nuevoautor:
                        libros['Autor'] = nuevoautor
                    if nuevoaño:
                        libros['Año'] = nuevoaño
                # Mostramos la nueva información del libro una vez editada.
                    print("\nEl libro se ha modificado con éxito.")
                    print(f"{clave} (Titulo: {libros['Titulo']}, Autor: {libros['Autor']}, Año: {libros['Año']})")
                    
                    respuesta = input("\n¿Desea modificar otro libro? s/n:  ")
                    if respuesta != 's':
                        break
                else:
                    print("Libro no encontrado.")
            # Pedimos valores enteros como ID válidas
            except ValueError:
                print("Por favor, ingrese una ID válida.")
        else:
            print("No hay libros por modificar.")
            break

# Aquí es el menú mostrado al usuario para que tenga opciones en el sistema de gestión bibliotecaria.

while True:
    print("\nSistema de organización para la biblioteca.\n")
    print("1. Agregar un libro.")
    print("2. Buscar un libro.")
    print("3. Listado de libros.")
    print("4. Eliminar un libro.")
    print("5. Modificar un libro.")
    print("6. Salir del sistema.")

    respuesta = input("\nSeleccione una de las opciones (1-6):  ")

# Ya si se escoge algun numero, el sitema activará la función para el usuario.

    if respuesta == '1':
        agregarlibro()
    elif respuesta == '2':
        buscarlibro()
    elif respuesta == '3':
        listadelibros()
    elif respuesta == '4':
        eliminarlibro()
    elif respuesta == '5':
        modificarlibro()
    elif respuesta == '6':
        print("Gracias por usar el sistema.")
        break
# Si no se escoge la opción correcta, pide algún valor válido.l
    else:
        print("Valor incorrecto, intente nuevamente.")
