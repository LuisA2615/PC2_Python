# Inicialización de contadores y lista
cantidad_pares = 0
cantidad_impares = 0
numeros_ingresados = []

while True:
    # Solicitar al usuario que ingrese un número
    numero = input("Ingresa un número (o escribe 'salir' para terminar): ")

    # Opción para salir del bucle
    if numero.lower() == 'salir':
        break

    # Intentar convertir el ingreso a un número
    try:
        numero = int(numero)  # Convertir a entero
        numeros_ingresados.append(numero)  # Agregar a la lista

        # Verificar si el número es par o impar
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Mostrar resultados
print("Números ingresados:", numeros_ingresados)
print(f"Números pares: {cantidad_pares}")
print(f"Números impares: {cantidad_impares}")

  
