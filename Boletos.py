# ¡Hola! Aquí empieza el código para crear un boleto de avión, buscarlo y calcular los totales que hay en este.
# Creamos un diccionario con fechas para que el usuario tenga la opción de elegir que días hay disponibles para el vuelo.
Boletos = {
    "11/05": {

    },
    "12/05": {

    },
    "13/05": {

    }
}

IDBOLETO = 1
# Estas listas las usaremos para definir valores individuales dependiendo de las elecciones del usuario.
totalgeneral = []
totalfecha1 = []
totalfecha2 = []
totalfecha3 = []
nacional = []
internacional = []
totalpasajeros = []
# De paso importamos una librería de colores para darle presentación al código.
from colorama import Fore, Style, init
init(autoreset=True)

def creaciondeboleto():
    # Llamamos cada una de las listas para poder añadir valores independientemente de lo que escoja el usuario.
    global IDBOLETO
    global nacional
    global internacional
    global totalpasajeros
    # Creamos un bucle para crear un boleto.
    while True:
            print(f"\n{Fore.BLUE}Bienvenido a la creación de su boleto.{Style.RESET_ALL}\n")
            while True:
                # Aquí se verifica si el nombre solo lleva letras, no se admiten otro tipo de valores.
                Nombre = input("Ingrese su nombre:  ")
                if any(caracter.isdigit() for caracter in Nombre):
                    print(f"\n{Fore.RED}Solo se aceptan letras en el nombre.{Style.RESET_ALL}\n")
                else:
                    break
            while True:
                # Aquí se define una variable de precio según el tipo de viaje, también el precio y se agrega a la lista nacional e internacional.
                TdV = input("¿Su viaje es hacia 1. Medellín o 2. España?:  ")
                if TdV == '1':
                    Viaje = "Medellín"
                    preciov = 230000
                    nacional.append(1)
                    break
                elif TdV == '2':
                    Viaje = "España"
                    preciov = 4200000
                    internacional.append(1)
                    break
                else:
                    # En cada bucle habrá un aviso si no se cumplen los requisitos para un valor requerido para el boleto.
                    print(f"\n{Fore.RED}Valor no valido, intente nuevamente eligiendo el 1 o 2.{Style.RESET_ALL}\n")
            while True:
                try:
                    # Aquí se revisa el peso del equipaje y se pone un precio según el peso, si el peso es mayor al indicado, se le drán opciones al usuario de viajar con el equipaje o no.
                    Equipaje = float(input("Ingrese el peso de su equipaje principal:  "))
                    if Equipaje > 50:
                        print(f"\nEl peso del equipaje {Fore.RED}excede los limites permitidos.{Style.RESET_ALL}\n")
                        Pregunta = input("¿Desea viajar sin el equipaje? s/n:  ").lower().strip()
                        if Pregunta == "s":
                            print(f"\n{Fore.LIGHTBLUE_EX}Viajará sin el equipaje.{Style.RESET_ALL}\n")
                            estado = "Viaja sin el equipaje."
                            precio = 0
                            break
                        elif Pregunta == "n":
                            print(f"\n{Fore.RED}Ingrese nuevamente el peso del equipaje.{Style.RESET_ALL}\n")
                        else:
                            print(f"\n{Fore.RED}Ingrese nuevamente el peso del equipaje.{Style.RESET_ALL}\n")
                    elif Equipaje > 30 and Equipaje <= 50:
                        precio = 110000
                        estado = "Viaja con el equipaje."
                        break
                    elif Equipaje > 20 and Equipaje <= 30:
                        precio = 70000
                        estado = "Viaja con el equipaje."
                        break
                    elif Equipaje > 0 and Equipaje <= 20:
                        precio = 50000
                        estado = "Viaja con el equipaje."
                        break
                    else:
                        # También validamos que los pesos sean positivos.
                        print(f"\n{Fore.RED}Ingrese un peso válido.{Style.RESET_ALL}\n")
                except ValueError:
                    # Con la validación de que solo sean números los que se ingresan en el equipaje.
                    print(f"\n{Fore.RED}Solo se permiten números como valor de equipaje.{Style.RESET_ALL}\n")
            while True:
                try:
                    # Creamos una variable para determinar el estado del equipaje de mano.
                    edm2 = ""
                    EdM = input("¿Lleva equipaje de mano? 1. Sí 2. No:  ")
                    if EdM == '1':
                        peso = float(input("¿Cuanto pesa su equipaje de mano?:  "))
                        # Le damos las opciones en dado caso de que el equipaje sea mayor o nulo al adecuado.
                        if peso > 13 or peso < 0:
                            print(f"\nEl equipaje es {Fore.RED}mayor o nulo al adecuado.{Style.RESET_ALL}\n")
                            pregunta = input("¿Desea viajar sin el equipaje de mano? s/n:  ") 
                            if pregunta == 's':
                                print(f"\n{Fore.LIGHTCYAN_EX}Viajará sin el equipaje de mano.{Style.RESET_ALL}\n")
                                edm2 = "Viajará sin el equipaje de mano."
                                break
                            elif pregunta == 'n':
                                print(f"\n{Fore.BLUE}Ingrese nuevamente el peso de su equipaje de mano.{Style.RESET_ALL}\n")
                            else:
                                print("Intente nuevamente ingresando 's' o 'n'.")
                        else:
                            print(f"\n{Fore.LIGHTCYAN_EX}Viajará con el equipaje de mano.{Style.RESET_ALL}\n")
                            edm2 = "Viajará con el equipaje de mano."
                            break
                    elif EdM == '2':
                        print(f"\n{Fore.LIGHTCYAN_EX}Viajará sin el equipaje de mano.{Style.RESET_ALL}\n")
                        edm2 = "Viajará sin el equipaje de mano."
                        break
                except ValueError:
                    print(f"\n{Fore.RED}Caracteres incorrectos, intente nuevamente.{Style.RESET_ALL}\n")
            # Aquí calculamos los costos de este boleto.
            Costo = int(preciov) + int(precio)        
            while True:
                # Una vez escogida la fecha, se agregara el costo a una lista dependiendo de la fecha.
                fecha = input("Eliga la fecha en la que va a viajar: 1. 11/05 2. 12/05 3. 13/05:  ")
                if fecha == '1':
                    clave = "11/05"
                    fechab = "11 de Mayo"
                    totalfecha1.append(Costo)
                    break
                elif fecha == '2':
                    clave = "12/05"
                    fechab = "12 de Mayo"
                    totalfecha2.append(Costo)
                    break
                elif fecha == '3':
                    clave = "13/05"
                    fechab = "13 de Mayo"
                    totalfecha3.append(Costo)
                    break
                else:
                    print(f"\n{Fore.RED}Valor incorrecto, intente nuevamente eligiendo del 1 al 3.{Style.RESET_ALL}\n.")
            # Creamos la ID del boleto para poderlo buscar más adelante.
            ID = f"{IDBOLETO:04d}"
            IDREAL = "COMP" + ID 
            # Añadimos el boleto al registro general.
            totalgeneral.append(Costo)
            totalpasajeros.append(1)
            
            # Creamos las claves para nuestro boleto.
            registro = {"Nombre del pasajero": Nombre, 
                        "Destino": Viaje, 
                        "Fecha": fechab, 
                        "Estado de Equipaje principal": estado, 
                        "Estado del equipaje de mano": edm2, 
                        "Costo total del viaje": Costo }
            IDBOLETO += 1
            # Lo guardamos en la fecha elegida con la ID automática.
            Boletos[clave][IDREAL] = registro
            # Le mostramos el boleto al usuario.
            print(f"\n{Fore.GREEN}Boleto registrado:{Style.RESET_ALL}\n")
            for clave, valor in registro.items():
                    print(f"{Fore.LIGHTCYAN_EX}{clave}{Style.RESET_ALL}: {valor}")
            # Preguntamos si queremos otro boleto, en dado caso de que no quiera añadir más, volverá al menú.
            pre = input(f"\n{Fore.BLUE}¿Desea añadir otro boleto? 1. Marque 1 para 'Sí'. 2. Marque cualquier opción para salir. :  {Style.RESET_ALL}")
            if pre != '1':
                break
            else:
                print(f"\n{Fore.BLUE}Añada otro boleto.{Style.RESET_ALL}")

# Las funciones que tienen fechas contean y suman cuanto se recaudo en cada día y cuanto se recaudo en general.
def totalfecha11():
    # En cada una se llama la lista de su fecha indicada.
    global totalfecha1
    # Se suman todos los valores.
    resultado = sum(totalfecha1)
    # Y finalmente se imprimen al usuario.
    print(f"\nEl total recaudado para el {Fore.CYAN}11 de Mayo{Style.RESET_ALL} es de {Fore.GREEN}${resultado}{Style.RESET_ALL}")

def totalfecha12():
    global totalfecha2
    resultado = sum(totalfecha2)
    print(f"\nEl total recaudado para el {Fore.CYAN}12 de Mayo{Style.RESET_ALL} es de {Fore.GREEN}${resultado}{Style.RESET_ALL}")

def totalfecha13():
    global totalfecha3
    resultado = sum(totalfecha3)
    print(f"\nEl total recaudado para el {Fore.CYAN}13 de Mayo{Style.RESET_ALL} es de {Fore.GREEN}${resultado}{Style.RESET_ALL}")

def totalreal():
    global totalgeneral
    resultado = sum(totalgeneral)
    print(f"\nEl total recaudado de {Fore.CYAN}todas las fechas{Style.RESET_ALL} es de {Fore.GREEN}${resultado}{Style.RESET_ALL}")
# Cree un menú para mirar cuánto se ha recaudado en cada fecha, esto solo en caso de que hayan boletos, si no se han registrado boletos aún, no dejará ver cuanto se ha logrado recaudar.
def totalmenu():
    hay_boletos = any(len(boleto) > 0 for boleto in Boletos.values())

    if not hay_boletos:
        print(f"\n{Fore.RED}No hay boletos registrados aún. Intenta registrar uno primero.{Style.RESET_ALL}")
        return
    while True:
        print(f"\n{Fore.BLUE}Totales disponibles.{Style.RESET_ALL}\n")
        print("1. Total recaudado.")
        print("2. Total 11 de Mayo.")
        print("3. Total 12 de Mayo.")
        print("4. Total 13 de Mayo.")
        print("5. Volver al menú.")

        pre = input(f"\n{Fore.BLUE}Escoge una de las opciones (1-5):   {Style.RESET_ALL}")
            
        if pre == '1':
                totalreal()
        elif pre == '2':
                totalfecha11()
        elif pre == '3':
                totalfecha12()
        elif pre == '4':
                totalfecha13()
        elif pre == '5':
            break
        else:
            print(f"\n{Fore.RED}Intente nuevamente escogiendo del 1 al 5.{Style.RESET_ALL}\n")


# Para los vuelos se realiza el mismo proceso que en la recaudación.
def vuelosnacionales():
    # Llamamos la lista de el tipo de vuelo.
    global nacional
    # Sumamos los vuelos contados para el tipo de cantidad.
    total = sum(nacional)
    # Y final se le imprime al usuario la cantidad de vuelos contados.
    print(f"\nEl total de pasajeros para {Fore.CYAN}vuelos nacionales{Style.RESET_ALL} es de: {Fore.GREEN}{total}{Style.RESET_ALL}")

def vuelosinternacionales():
    global internacional
    total = sum(internacional)
    print(f"\nEl total de pasajeros para {Fore.CYAN}vuelos internacionales{Style.RESET_ALL} es de: {Fore.GREEN}{total}{Style.RESET_ALL}")

def vuelostotales():
    global totalpasajeros
    total = sum(totalpasajeros)
    print(f"\nEl total de pasajeros para {Fore.CYAN}todos los vuelos{Style.RESET_ALL} es de: {Fore.GREEN}{total}{Style.RESET_ALL}")

# Aquí es el menú de los vuelos contados, funciona igual que el menú principal y el de recaudación, aquí también se verifican que hayan boletos disponibles, en caso de no haber, no deja visualizar las cantidades contadas.
def pasajerosmenu():
    hay_boletos = any(len(boleto) > 0 for boleto in Boletos.values())

    if not hay_boletos:
        print(f"\n{Fore.RED}No hay boletos registrados aún. Intenta registrar uno primero.{Style.RESET_ALL}")
        return
    
    while True:
        print(f"\n{Fore.BLUE}Cantidad de pasajeros.{Style.RESET_ALL}\n")
        print("1. Cantidad de pasajeros en total.")
        print("2. Cantidad de pasajeros nacionales.")
        print("3. Cantidad de pasajeros internacionales.")
        print("4. Volver al menú.")

        res = input(f"\n{Fore.BLUE}Ingrese una opción (1-4):  {Style.RESET_ALL}")

        if res == '1':
            vuelostotales()
        elif res == '2':
            vuelosnacionales()
        elif res == '3':
            vuelosinternacionales()
        elif res == '4':
            break
        else:
            print(f"\n{Fore.RED}Por favor, ingrese una opción válida (1-4).{Style.RESET_ALL}")

# Para buscar un boleto se mira también si hay boletos disponibles.
def buscarboleto():
    hay_boletos = any(len(boleto) > 0 for boleto in Boletos.values())

    if not hay_boletos:
        print(f"\n{Fore.RED}No hay boletos registrados aún. Intenta registrar uno primero.{Style.RESET_ALL}")
        return
    # En dado caso de haber, buscamos por su ID, si la ID no es encontrada mostrará el aviso, de lo contrario, se le dirá al usuario la información completa del boleto.
    while True:
        print(f"\n{Fore.BLACK}Busca un boleto{Style.RESET_ALL}\n")
        Boleto_Buscado = input(f"{Fore.BLUE}Ingrese la ID de su boleto (ej: COMP0001):  {Style.RESET_ALL}").upper().strip()
        encontrado = False
        for fecha, boleto in Boletos.items():
            if Boleto_Buscado in boleto:
                print(f"\n{Fore.GREEN}El boleto ha sido encontrado para la fecha: {fecha}{Style.RESET_ALL}\n")
                for clave, valor in boleto[Boleto_Buscado].items():
                    print(f"{Fore.LIGHTCYAN_EX}{clave}{Style.RESET_ALL}: {valor}")
                    encontrado = True

        if not encontrado:
            print(f"\n{Fore.RED}El boleto no ha sido encontrado.{Style.RESET_ALL}")
        # Una vez se encuentre en boleto, volverá al menú principal.
        else:
            break


# Finalmente llegamos al menú principal, donde el admin puede ver todo los procesos contados y registrados.
while True:
    print(f"\n{Fore.BLUE}Boletos de Aerolínea.\n{Style.RESET_ALL}")
    print("1. Agregar un boleto.")
    print("2. Costo total de las compras.")
    print("3. Número de vuelos.")
    print("4. Buscar un boleto.")
    print("5. Salir.")

    pregunta = input(f"\n{Fore.BLUE}Ingrese una opción (1-5):  {Style.RESET_ALL}")
    # El usuario si o si tiene que escoger una de las opciones mostradas, si no lo hace, se le dará un aviso.
    if pregunta == '1':
        creaciondeboleto()
    elif pregunta == '2':
        totalmenu() 
    elif pregunta == '3':
        pasajerosmenu()
    elif pregunta == '4':
        buscarboleto()
    elif pregunta == '5':
        # Una vez el usuario esté satisfecho, tendrá la opción de salir del sistema.
        print(f"\n{Fore.GREEN}Gracias por usar el sistema, vuelva pronto.{Style.RESET_ALL}\n")
        break
    else:
        print(f"\n{Fore.RED}Por favor ingrese una opción válida (1-5).{Style.RESET_ALL}")