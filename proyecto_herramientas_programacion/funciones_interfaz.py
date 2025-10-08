from funciones_almacen_farmacos import modulos, estado_modulos
from funciones_pedidos_farmacos import pedido_en_proceso, pedido_por_procesar,procesar_pedido


def interfaz():
    import sys
    while True:    
        print("""
        Main menu 

        1 - Información general. 
        2 - Estado del Almacén. 
        3 - Pedidos. 
        4 - Informes históricos. 
        5 - Salir del programa.
        """)

        seleccion = input("Introduce un número: ")

        if seleccion == "1":
            interfaz_1()
        elif seleccion == "2":
            interfaz_2()
        elif seleccion == "3":
            interfaz_3()
        elif seleccion == "4":
            interfaz_4()
        elif seleccion == "5":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida.")
            interfaz()


def interfaz_1():
    
    print("""
    Información general
        
        
    B - Vuelve al menú anterior.
    """)
    seleccion_1 = input("Selecciona una opción: ")
    if seleccion_1.upper() == "B":
        interfaz()


def interfaz_2():
      
    print("""
    Estado del Almacén

    1 - Mostrar los módulos del almacén. 
    2 - Mostrar el estado de un módulo. 
    B - Vuelve al menú anterior.
    """) 

    seleccion_2 = input("Selecciona una opción: ")
    if seleccion_2.upper() == "B":
        interfaz()
            
    elif seleccion_2 == "1":
        print("Mostrando los módulos del almacén...")
        interfaz_2_1()
    elif seleccion_2 == "2":
        print("Mostrando el estado de un módulo...")
        interfaz_2_2()
    else:
        print("Opción no válida.")
        interfaz_2()
    
def interfaz_2_1():
    modulos()
    print("B - Vuelve al menú anterior.")
    seleccion_2_1 = input("Selecciona una opcion:")

    if seleccion_2_1.upper() == 'B':
        interfaz_2()
    else:
        print("Opción no válida.")
        interfaz_2_1()

def interfaz_2_2():
    estado_modulos()
    print("B - Vuelve al menú anterior.")
    seleccion_2_2 = input("Selecciona una opcion:")
    
    if seleccion_2_2.upper() == 'B':
        interfaz_2()
    else:
        print("Opción no válida.")
        interfaz_2_2()

def interfaz_3():   
    print("""
    Pedidos

    1 - Mostrar los pedidos sin procesar. 
    2 - Procesar pedido.
    3 - Revertir Proceso de pedido
    4 - Mostrar los pedidos en marcha. 
    5 - Nuevo Pedido
    B - Vuelve al menú anterior.
        """) 
    
    seleccion_3 = input("Selecciona una opción: ")

    if seleccion_3 == "1":
        interfaz_3_1() 
    elif seleccion_3 == "2":
        interfaz_3_2()
    elif seleccion_3 == "3":
        interfaz_3_3()
    elif seleccion_3 == "4":
        interfaz_3_4()
    elif seleccion_3 == "5":
        interfaz_3_5()
    elif seleccion_3.upper() == "B":
        interfaz()    
    else:
        print("Opción no válida.")
        interfaz_3()

def interfaz_3_1():
    
    pedido_por_procesar()
    print()
    print("B - Vuelve al menú anterior.")
    
    seleccion_3_1 = input("Selecciona una opción: ")

    if seleccion_3_1.upper() == "B":
        interfaz_3()
    else:
        print("Opción no válida.")
        interfaz_3_1()

def interfaz_3_2():
    
    procesar_pedido()
    print()
    print("B - Vuelve al menú anterior.")
    
    seleccion_3_1 = input("Selecciona una opción: ")

    if seleccion_3_1.upper() == "B":
        interfaz_3()
    else:
        print("Opción no válida.")
        interfaz_3_2()

def interfaz_3_3():
    print()

def interfaz_3_4():

    pedido_en_proceso()
    print()
    print("B - Vuelve al menú anterior.")

    seleccion_3_1 = input("Selecciona una opción: ")

    if seleccion_3_1.upper() == "B":
        interfaz_3()
    else:
        print("Opción no válida.")
        interfaz_3_1()

def interfaz_3_5():
    print()


def interfaz_4():
      
    print("""
    Informes históricos

    [En construcción]
        
    B - Vuelve al menú anterior.
    """)
    seleccion_4 = input("Selecciona una opción: ")
        
    if seleccion_4.upper() == "B":
        interfaz()
    