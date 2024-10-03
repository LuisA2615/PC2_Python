def es_numero_perfecto(n):
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores == n

def encontrar_numeros_perfectos(limite):
    numeros_perfectos = []
    for i in range(1, limite):
        if es_numero_perfecto(i):
            numeros_perfectos.append(i)
    return numeros_perfectos

resultado = encontrar_numeros_perfectos(1000)
print("Números perfectos menores que 1000:", resultado)