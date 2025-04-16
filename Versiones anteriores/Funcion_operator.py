import operator
def operar(i, c, operador):
    operaciones = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
    "NAND": operator.not_

    }
    
    resultado = operaciones[operador](i, c)
    return resultado




# Aqui solicita un valor y validando que solo se ingrese 0 o 1
def pedir_valor(mensaje):
    while True:
        valor = input(mensaje)
        if valor in ['0', '1']:  # Si es 0 o 1, lo convierte a entero y lo devuelve
            return int(valor)
        else:
            print("Por favor, ingresá solo 0 o 1.")  # Si no, muestra un mensaje de error

def funcion_operacion():

    if operador != "NOT":  
        print(f"\n--- TABLA DE VERDAD: {operador} ---")
        print(f"A | B | A {operador} B")
        for i in range (0, 2):
            for c in range (0, 2):
                x = operar(i, c, operador)
                print(f"{i} | {c} |   {x}")
    elif operador == "NOT":
        print(f"\n--- TABLA DE VERDAD: {operador} ---")
        print(f"A | {operador} A")
        for i in range (0, 2):
            x = int(not i)
            print(f"{i} |   {x}")


ejecutando = True
while ejecutando:
    print("\n*************\n* SIMULADOR *\n*************")
    print("A - Operación AND")
    print("O - Operación OR")
    print("N - Operación NOT")
    print("X - Operación XOR")
    print("Y - Operacion NAND")
    print("Z - Operacion NOR")
    print("S - Salir")

    opcion = input("Seleccioná una opción: ").upper()

    if opcion == "A":
        operador = "AND"
        funcion_operacion()
    elif opcion == "O":
        operador = "OR"
        funcion_operacion()
    elif opcion == "N":
        operador = "NOT"
        funcion_operacion()
    elif opcion == "X":
        operador = "XOR"
        funcion_operacion()
    elif opcion == "Y":
        operador = "NAND"
        funcion_operacion()
    elif opcion == "Z":
        operador = "NOR"
        funcion_operacion()
    elif opcion == "S":
        print("¡Gracias por usar el simulador del grupo 2! 👋")
        ejecutando = False  # Cambia la condición para salir del bucle
    else:
        print("Opción no válida. Probá otra vez.")
