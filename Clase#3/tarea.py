def multiplicar(a, b):
    resultado = 0
    for _ in range(abs(b)):
        resultado += abs(a)
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return -resultado
    return resultado

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    cociente = 0
    resto = abs(a)
    divisor = abs(b)
    while resto >= divisor:
        resto -= divisor
        cociente += 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return -cociente
    return cociente

def triangulo_numeros(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(multiplicar(i, j), end=" ")
        print()
        # Ejemplo de uso
n = int(input("Ingrese la altura del triángulo: "))
triangulo_numeros(n)
 