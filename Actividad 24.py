def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sumaNumerosN(n):
    if n == 1:
        return 1
    else:
        return n + sumaNumerosN(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def contarLetra(palabra, letra, indice=0):
    if indice == len(palabra):
        return 0
    return (1 if palabra[indice] == letra else 0) + contarLetra(palabra, letra, indice + 1)


def invertirCadena(cadena):
    if len(cadena) == 0:
        return ""
    return cadena[-1] + invertirCadena(cadena[:-1])

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base,exponente - 1)

while True:
    print("1. Calcular factorial de un número")
    print("2. Suma de los números N de números naturales")
    print("3. Calcular el n-ésimo número de Fibonacci")
    print("4. Contar cuántas veces aparece una letra en una palabra")
    print("5. Invertir una cadena de texto")
    print("6. Calcular la potencia de un número (base^exponente)")
    print("7. Salir del programa")
    opcion = input("(1 - 7): ")

    match opcion:
        case "1":
            print()
            n = int(input("Ingrese el número del que quiere saber el factorial: "))
            x = factorial(n)
            print(f"El factorial de {n} es {x}")
            print()

        case "2":
            print()
            n = int(input("Ingrese el numero que quiere sumar: "))
            if n > 0:
                x = sumaNumerosN(n)
                print(f"La suma de todos los numeros naturales desde 1 hasta {n} es {x}")
            else:
                print("Número no válido")
            print()

        case "3":
            print()
            n = int(input("Ingrese el número: "))
            x = fibonacci(n)
            print(f"El numero de fibonacci de {n} es {x}")
            print()

        case "4":
            y = input("Ingrese la palabra: ")
            z = input("Ingrese la letra: ")
            x = contarLetra(y, z)
            print()
            print(f"La letra {z}, aparece {x} veces en la palabra {y}")
            print()

        case "5":
            n = input("Ingrese la palabra a invertir: ")
            x = invertirCadena(n)
            print(f"La palabra {n} invertida es: {x}")
            print()

        case "6":
            n = int(input("Ingerese la base: "))
            y = int(input("Ingrese el exponente: "))
            x = potencia(n, y)
            print(f"La potencia de {n} a la {y} es: {x}")
            print()

        case "7":
            print("Cerraste el programa!")
            break

        case _:
            print("Opcion invalida, vuelve a intenarlo")
            print()