from colorama import init, Fore
import time

# Inicializo colorama para poder usar colores en la terminal sin preocuparnos por reiniciar el estilo manualmente
init(autoreset=True)

# Esta función la hicimos para asegurarme de que el usuario solo pueda ingresar 0 o 1
def pedir_valor(mensaje):
    while True:
        valor = input(Fore.YELLOW + mensaje)
        if valor in ['0', '1']:
            return int(valor)
        else:
            print(Fore.RED + "Por favor, ingresá solo 0 o 1.")

# Acá creamos una función que convierte un número decimal a binario de 8 bits, mostrando todo el proceso paso a paso
def funcion_conversor_d_a_b():
    titulo = f'''
{Fore.CYAN}{'*'*90}
Esta parte del programa convierte números decimales (máximo 255) a número binario (8 bits)
{'*'*90}
'''
    print(titulo)

    binario_cadena = ''

    # Nos aseguramos de que el número ingresado esté dentro del rango permitido (0 a 255)
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

    # Este bloque muestra cómo va dividiendo el número entre 2 y guardando los restos (como se hace a mano)
    print(Fore.MAGENTA + "\nConvirtiendo a binario paso a paso:\n")
    while numero_d > 0:
        resto = numero_d % 2
        pasos.append(resto)
        print(Fore.BLUE + f"→ {numero_d} ÷ 2 = {numero_d // 2} | Resto = {resto}")
        time.sleep(0.5)  # Le pusimos una pausa para que se vea el proceso más animado
        numero_d = numero_d // 2

    # Se arma el binario con los restos, invirtiendo el orden y rellenando con ceros si hace falta
    binario_cadena = ''.join(str(bit) for bit in reversed(pasos)).zfill(8)

    print(Fore.GREEN + f"\nResultado final: El número decimal {ingreso_decimal} en binario (8 bits) es: {binario_cadena}")
    print(Fore.CYAN + "✨ Conversión completada con éxito!!!! Ya estamos aprobados? ✨\n")

# Esta función la hicimos para mostrar una tabla de verdad dependiendo del operador lógico que elija el usuario
def funcion_operacion(operador):
    if operador != "NOT": #Se verficia que el operador no sea NOT, ya que utiliza una tabla diferente
        print(Fore.CYAN + f"\n--- TABLA DE VERDAD: {operador} ---")
        print(Fore.WHITE + f"A | B | A {operador} B") #Se imprime la cabecera de la tabla de verdad, con la variable operador
        for i in range(2): #comenzamos el primer loop, con un valor entre 0 y 1 (inclusive)
            for c in range(2):  #Se realiza otro loop dentro del primero, con el segundo valor, entre 0 y 1 (inclusive)
                if operador == "AND": #Pregunta primero si el operador es AND, en caso de no serlo, va consultando un por uno para realizar el calculo
                    x = i and c #Se almacena en X la operacion entre A y B (Variable i y c)
                elif operador == "OR": 
                    x = i or c
                elif operador == "XOR":
                    x = i ^ c           
                elif operador == "NAND":
                    x = int(not (i and c)) 
                elif operador == "NOR": 
                    x = int(not (i or c))
                print(f"{i} | {c} |   {x}") #Se imprime con un F string los 3 valores, las variables iteraticas i, c y el resultado x 

        # Pedimos los valores de entrada para hacer el cálculo personalizado
        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        b = pedir_valor("Ingresá el valor de B (0 o 1): ")
        resultado = calcular(a, b, operador)

    else:
        # Caso especial para el operador NOT que solo necesita un valor
        print(Fore.CYAN + f"\n--- TABLA DE VERDAD: {operador} ---")
        print(Fore.WHITE + f"A | {operador} A")
        for i in range(2):
            x = int(not i)
            print(f"{i} |   {x}")
        a = pedir_valor("\nIngresá el valor de A (0 o 1): ")
        resultado = int(not a)
        print(Fore.GREEN + f"Resultado de NOT {a} = {resultado}")

# Esta función simplemente ejecuta la operación lógica según el operador que se pasó como argumento
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

# Acá está el corazón del programa: un menú que repite hasta que el usuario decida salir
def main():
    ejecutando = True

    while ejecutando:
        print(Fore.MAGENTA + "\n*************\n* SIMULADOR *\n*************")
        print( "A - Operación AND")
        print("O - Operación OR")
        print("N - Operación NOT")
        print("X - Operación XOR")
        print("Y - Operación NAND")
        print("Z - Operación NOR")
        print("D - Conversor decimal a binario de 8 bits")
        print("S - Salir")

        opcion = input(Fore.YELLOW + "Seleccioná una opción: ").upper()

        # Según la opción que elija el usuario, llamo a la función correspondiente
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
            print(Fore.CYAN + "¡Hasta la próxima!")
            print(Fore.RED + "✨\n Ignacio Carné \n Gaspar Compagnucci\n Gabriel Carbajal\n Diego Carrizo\n Matías Carro\n Hugo Catalán✨\n")
            ejecutando = False
        else:
            print(Fore.RED + "Opción no válida. Probá otra vez.")

# Acá arranca todo, ejecuto la función principal
main()
# Fin del programa

