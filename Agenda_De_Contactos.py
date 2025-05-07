agenda = {}

def listadecontactos():
    # Nos aseguramos de que hayan contactos para mostar, en dado caso de que no hayan, lanzamos el mensaje.
    if not agenda:
        print("No hay contactos disponibles.")
    else:
        for nombre, contacto in agenda.items():
            print(f"{nombre} (Número: {contacto['Número']}, Correo: {contacto['Correo']})")

def agregarcontactos():
    #Usamos la agenda en general para realizar el agendado.
    global agenda
    while True:
        # Le pedimos al usuario que ingerese la información requerida para agregar un contacto.
        print("\n Agregue un contacto.")
        nombre = input("Ingrese el nombre del contacto:  ").lower()
        correo = input("Ingrese el correo:  ")
        # Nos aseguramos de que el número siempre sea un entero y no cualquier otro valor con el isdigit().
        while True:
            numero = input("Ingrese el numero de celular:  ")
            if numero.isdigit():
                break
            else:
                print("Por favor ingrese un número válido.")
        # En dado caso de que el nombre no esté en repetido, procederá a agregarlo al diccionario.
        if nombre not in agenda:
            num2 = str(numero)
            guardado = {'Número': num2, 'Correo': correo}
            agenda[f"{nombre}"] = guardado 
            print("Se ha agregado el contacto correctamente.")
            for nombre, contacto in agenda.items():
                print(f"{nombre} (Número: {contacto['Número']}, Correo: {contacto['Correo']})")
        # Aquí le pedimos al usuario si gusta agregar otro libro, en dado caso que la respuesta se distinta de "s o S", se termina la función.
            respuesta = input("¿Desea agregar otro? s/n:  ").lower()
            if respuesta != 's':
                break
        # Si ya hay un contacto con ese nombre, se repite el bucle y no agrega el contacto para no sobreescribir valores del diccionario.
        else:
            print("Ya hay un contacto con ese nombre, intente nuevamente.")

def modificarcontacto():
    while True:
        # En cada función habrá la condicional de que si hay contactos, proceder con la funcion, en cambio, mostrar que no hay contactos.
        if agenda:
            va = input("Ingrese el nombre del contacto que desea modificar:  ").lower()
            # Miramos si el contacto a modificar está en la agenda, en dado caso de que no esté, pone "Contacto no encontrado".
            if va in agenda:
                while True:
                    nuevonum = input("Ingrese el nuevo número de celular:  ")
                    if nuevonum.isdigit():
                        break
                    else:
                        print("Por favor ingrese un número válido.")
                # Aquí hacemos el cambio de los valores dentro de la clave asignada.
                nuevocorreo = input("Por favor ingrese su nuevo correo:  ")
                agenda[va]['Número'] = nuevonum
                agenda[va]['Correo'] = nuevocorreo
                print("La información del contacto se ha modificado con éxito.")
                print(f"{va} (Número:  {nuevonum}, Correo:  {nuevocorreo})")
            else:
                print("Contacto no encontrado.")
            respuesta = input("¿Desea modificar otro contacto? s/n:  ")
            if respuesta != 's':
                break
        else:
            print("No hay contactos para modificar.")
            break

def eliminarcontacto():
    while True:
        if agenda:
            # Mostramos los contactos disponibles antes de eliminar
            print("\nLista de contactos disponibles:")
            for nombre, contacto in agenda.items():
                print(f"{nombre} (Número: {contacto['Número']}, Correo: {contacto['Correo']})")
                
            # Pedimos el nombre del contacto a eliminar
            eliminar = input("Ingrese el nombre del contacto que desea eliminar: ").lower()

            if eliminar in agenda:
                # Eliminamos el contacto de la agenda
                del agenda[eliminar]
                print(f"El contacto '{eliminar}' ha sido eliminado exitosamente.")
                break  # Salir del bucle después de eliminar el contacto
            else:
                print("Contacto no encontrado. Intente nuevamente.")
        else:
            print("No hay contactos en la agenda para eliminar.")
            break  # Salir si no hay contactos para eliminar

while True:
    print("\nSistema de Agenda.")
    print("1. Agregar contacto")
    print("2. Ver lista de contactos")
    print("3. Modificar contacto")
    print("4. Eliminar un contacto")
    r = input()

    if r == '1':
        agregarcontactos()
    elif r == '2':
        listadecontactos()
    elif r == '3':
        modificarcontacto()
    elif r == '4':
        eliminarcontacto()
    else:
        print("Opción no válida. Intenta de nuevo.")
