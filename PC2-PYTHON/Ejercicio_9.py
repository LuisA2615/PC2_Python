def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    texto_sin_vocales = ''.join(char for char in texto if char not in vocales)
    return texto_sin_vocales

# Solicitar al usuario una cadena de texto
entrada_usuario = input("Ingresa una cadena de texto: ")
resultado = omitir_vocales(entrada_usuario)

print("Salida sin vocales:", resultado)