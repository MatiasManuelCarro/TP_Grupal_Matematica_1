# Aqui solicita un valor y validando que solo se ingrese 0 o 1
def pedir_valor(mensaje):
    while True:
        valor = input(mensaje) 
        if valor in ['0', '1']:  # Si es 0 o 1, lo convierte a entero y lo devuelve
            return int(valor)
        else:
            print("Por favor, ingresá solo 0 o 1.")  # Si no, muestra un mensaje de error

def funcion_operacion(operador):

    if operador != "NOT":  #Verificamos que el operador no sea NOT, ya que lleva una tabla distinta 
        print(f"\n--- TABLA DE VERDAD: {operador} ---")
        print(f"A | B | A {operador} B")
        for i in range (0, 2): #comenzamos el primer loop, con un valor entre 0 y 1 (inclusive)
            for c in range (0, 2): #Se realiza otro loop dentro del primero, con el segundo valor, entre 0 y 1 (inclusive)
                if operador == "AND": #Si el operador es AND, realizamos la operacion
                    x = i and c
                elif operador == "OR": 
                    x = i or c
                elif operador == "XOR": 
                    x = i ^  c
                elif operador == "NAND": 
                    x = int(not (i and c))
                elif operador == "NOR": 
                    x = int(not (i or c))
                print(f"{i} | {c} |   {x}") #Se imprime con un F string los 3 valores

        #Pedimos ingreso al usuario para que realize un calculo con la tabla de verdad
        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        b = pedir_valor("Ingresá el valor de B (0 o 1): ")
        resultado = calcular(a, b, operador) #asignamos a resultado lo que devuelve la funcion calcular()

    elif operador == "NOT": #En caso de que el operador sea NOT, utilizamos otra tabla de verdad
        print(f"\n--- TABLA DE VERDAD: {operador} ---")
        print(f"A | {operador} A")
        for i in range (0, 2): #se utiliza un solo ciclo for, porque la tabla requiere un solo valor
            x = int(not i) 
            print(f"{i} |   {x}") #imprimimos los valores en un f string

        #Pedimos ingreso al usuario para que realize un calculo con la tabla de verdad
        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        resultado = int(not a)
        print(f"Resultado de NOT {a} = {resultado}")

def calcular(a, b, operador): #Esta funcion realiza el calculo entre los dos numeros ingresados por el usuario
    #primero verificamos que operador selecciono el usuario
    if operador == "AND": 
        resultado = a and b #depeniendo de que operador haya seleccionado, realizamos la operacion
    elif operador == "OR":
        resultado = a or b
    elif operador == "XOR":
        resultado = a ^  b
    elif operador == "NAND":
        resultado = int(not (a and b))
    elif operador == "NOR":
        resultado = int(not (a or b))
    print(f"Resultado de {a} {operador} {b} = {resultado}") #devolvemos el resultado imprimiendolo en pantalla

def main():
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
            funcion_operacion(operador)
        elif opcion == "O":
            operador = "OR"
            funcion_operacion(operador)
        elif opcion == "N":
            operador = "NOT"
            funcion_operacion(operador)
        elif opcion == "X":
            operador = "XOR"
            funcion_operacion(operador)
        elif opcion == "Y":
            operador = "NAND"
            funcion_operacion(operador)
        elif opcion == "Z":
            operador = "NOR"
            funcion_operacion(operador)
        elif opcion == "S":
            print("¡Gracias por usar el simulador del grupo 2! 👋")
            ejecutando = False  # Cambia la condición para salir del bucle
        else:
            print("Opción no válida. Probá otra vez.")

main()