def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

suma_primos = sum(num for num in range(100) if es_primo(num))

print("La suma de todos los números primos menores que 100 es:", suma_primos)