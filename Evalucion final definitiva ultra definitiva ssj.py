def mostrar_menu():
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")

def pedir_opcion():
    opcion = int(input("Opción: "))
    return opcion

def validar_nombre(nombre):
    if nombre == "":
        return False
    else:
        return True

def validar_edad(edad):
    if edad > 0:
        return True
    else:
        return False

def validar_temperatura(temperatura):
    if temperatura >= 35.0 and temperatura <= 42.0:
        return True
    else:
        return False

def agregar_paciente(lista_pacientes):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    temperatura = float(input("Temperatura: "))
    
    if validar_nombre(nombre) == False:
        print("El nombre no puede estar vacío.")
    elif validar_edad(edad) == False:
        print("La edad debe ser mayor que cero.")
    elif validar_temperatura(temperatura) == False:
        print("La temperatura debe estar entre 35.0 y 42.0.")
    else:
        paciente = {}
        paciente["nombre"] = nombre
        paciente["edad"] = edad
        paciente["temperatura"] = temperatura
        paciente["atendido"] = False
        lista_pacientes.append(paciente)
        print("Registrado con éxito.")

def buscar_paciente(lista_pacientes, nombre_buscar):
    posicion = 0
    for paciente in lista_pacientes:
        if paciente["nombre"] == nombre_buscar:
            return posicion
        posicion = posicion + 1
    return -1

def eliminar_paciente(lista_pacientes):
    nombre_eliminar = input("Nombre a eliminar: ")
    posicion = buscar_paciente(lista_pacientes, nombre_eliminar)
    if posicion == -1:
        print("El paciente '" + nombre_eliminar + "' no se encuentra registrado.")
    else:
        lista_pacientes.pop(posicion)
        print("Paciente eliminado correctamente.")

def actualizar_estado(lista_pacientes):
    for paciente in lista_pacientes:
        if paciente["temperatura"] <= 37.0:
            paciente["atendido"] = True
        else:
            paciente["atendido"] = False

def mostrar_pacientes(lista_pacientes):
    actualizar_estado(lista_pacientes)
    for paciente in lista_pacientes:
        print("Nombre:", paciente["nombre"])
        print("Edad:", paciente["edad"])
        print("Temperatura:", paciente["temperatura"])
        if paciente["atendido"] == True:
            print("Estado: ATENDIDO")
        else:
            print("Estado: REQUIERE ATENCION")

lista_general = []
opcion_elegida = 0

while opcion_elegida != 6:
    mostrar_menu()
    opcion_elegida = pedir_opcion()
    
    if opcion_elegida == 1:
        agregar_paciente(lista_general)
        
    elif opcion_elegida == 2:
        nombre_buscar = input("Nombre a buscar: ")
        posicion = buscar_paciente(lista_general, nombre_buscar)
        if posicion != -1:
            paciente_encontrado = lista_general[posicion]
            print("Nombre:", paciente_encontrado["nombre"])
            print("Edad:", paciente_encontrado["edad"])
            print("Temperatura:", paciente_encontrado["temperatura"])
            if paciente_encontrado["atendido"] == True:
                print("Estado: ATENDIDO")
            else:
                print("Estado: REQUIERE ATENCION")
        else:
            print("Mensaje: Paciente no encontrado.")
            
    elif opcion_elegida == 3:
        eliminar_paciente(lista_general)
        
    elif opcion_elegida == 4:
        actualizar_estado(lista_general)
        print("Estados actualizados.")
        
    elif opcion_elegida == 5:
        mostrar_pacientes(lista_general)
        
    elif opcion_elegida == 6:
        print("Gracias por usar el sistema. Vuelva Pronto. Chao nomah")
