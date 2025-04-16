from colorama import init, Fore
import time

# Inicializamos colorama
init(autoreset=True)

# Función para pedir un valor 0 o 1 validado
def pedir_valor(mensaje):
    while True:
        valor = input(Fore.YELLOW + mensaje)
        if valor in ['0', '1']:
            return int(valor)
        else:
            print(Fore.RED + "Por favor, ingresá solo 0 o 1.")

# Función para convertir decimal a binario (8 bits) con animación y color
def funcion_conversor_d_a_b():
    titulo = f'''
{Fore.CYAN}{'*'*90}
  Esta parte del programa convierte números decimales (máximo 255) a número binario (8 bits)
{'*'*90}
'''
    print(titulo)

    binario_cadena = ''

    # Validamos el ingreso
    while True:
        try:
            ingreso_decimal = int(input(Fore.YELLOW + 'Ingrese un número decimal (máximo 255): '))
            if 0 <= ingreso_decimal <= 255:
                break
            else:
                print(Fore.RED + 'Ingreso fuera de rango. Ingresá un número entre 0 y 255.')
        except ValueError:
            print(Fore.RED + 'Error: Ingresá un número válido.')

    numero_d = ingreso_decimal
    pasos = []

    # Mostramos el proceso de conversión
    print(Fore.MAGENTA + "\nConvirtiendo a binario paso a paso:\n")
    while numero_d > 0:
        resto = numero_d % 2
        pasos.append(resto)
        print(Fore.BLUE + f"→ {numero_d} ÷ 2 = {numero_d // 2} | Resto = {resto}")
        time.sleep(0.5)
        numero_d = numero_d // 2

    binario_cadena = ''.join(str(bit) for bit in reversed(pasos)).zfill(8)

    print(Fore.GREEN + f"\nResultado final: El número decimal {ingreso_decimal} en binario (8 bits) es: {binario_cadena}")
    print(Fore.CYAN + "✨ Conversión completada con éxito ✨\n")

# Función para mostrar tabla de verdad y pedir operación lógica
def funcion_operacion(operador):
    if operador != "NOT": #Se verficia que el operador no sea NOT, ya que utiliza una tabla diferente 
        print(Fore.CYAN + f"\n--- TABLA DE VERDAD: {operador} ---")
        print(Fore.WHITE + f"A | B | A {operador} B") #Se imprime la cabecera de la tabla de verdad, con la variable operador
        for i in range(2): #comenzamos el primer loop, con un valor entre 0 y 1 (inclusive)
            for c in range(2):  #Se realiza otro loop dentro del primero, con el segundo valor, entre 0 y 1 (inclusive)
                if operador == "AND": #Si el operador es AND, se calcula la operacion AND entre las dos variables iterativas i, c
                    x = i and c
                elif operador == "OR": #Lo mismo para OR
                    x = i or c
                elif operador == "XOR": 
                    x = i ^ c           #Se realiza el calculo para XOR
                elif operador == "NAND":
                    x = int(not (i and c)) #Se realiza el calculo para NAND
                elif operador == "NOR":
                    x = int(not (i or c)) #Por ultimo se realiza el calculo para NOR
                print(f"{i} | {c} |   {x}") #Se imprime con un F string los 3 valores, las variables iteraticas i, c y el resultado x 

        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        b = pedir_valor("Ingresá el valor de B (0 o 1): ")
        resultado = calcular(a, b, operador)

    else:
        print(Fore.CYAN + f"\n--- TABLA DE VERDAD: {operador} ---")
        print(Fore.WHITE + f"A | {operador} A")
        for i in range(2):
            x = int(not i)
            print(f"{i} |   {x}")
        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        resultado = int(not a)
        print(Fore.GREEN + f"Resultado de NOT {a} = {resultado}")

# Función que calcula una operación lógica entre A y B
def calcular(a, b, operador):
    if operador == "AND":
        resultado = a and b
    elif operador == "OR":
        resultado = a or b
    elif operador == "XOR":
        resultado = a ^ b
    elif operador == "NAND":
        resultado = int(not (a and b))
    elif operador == "NOR":
        resultado = int(not (a or b))
    print(Fore.GREEN + f"Resultado de {a} {operador} {b} = {resultado}")
    return resultado

# Función principal del programa
def main():
    ejecutando = True

    while ejecutando:
        print(Fore.MAGENTA + "\n*************\n* SIMULADOR *\n*************")
        print(Fore.CYAN + "A - Operación AND")
        print("O - Operación OR")
        print("N - Operación NOT")
        print("X - Operación XOR")
        print("Y - Operación NAND")
        print("Z - Operación NOR")
        print("D - Conversor decimal a binario de 8 bits")
        print("S - Salir")

        opcion = input(Fore.YELLOW + "Seleccioná una opción: ").upper()

        if opcion == "A":
            funcion_operacion("AND")
        elif opcion == "O":
            funcion_operacion("OR")
        elif opcion == "N":
            funcion_operacion("NOT")
        elif opcion == "X":
            funcion_operacion("XOR")
        elif opcion == "Y":
            funcion_operacion("NAND")
        elif opcion == "Z":
            funcion_operacion("NOR")
        elif opcion == "D":
            funcion_conversor_d_a_b()
        elif opcion == "S":
            print(Fore.CYAN + "\n¡Gracias por usar el simulador del grupo 2! 👋\n")
            ejecutando = False
        else:
            print(Fore.RED + "Opción no válida. Probá otra vez.")

# Ejecutamos el programa
main()
# Fin del programa