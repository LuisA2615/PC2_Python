def calcular_factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")