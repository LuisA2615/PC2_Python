# Lista de alumnos
alumnos = []

# Ingreso de la cantida de alumnos
n = int(input("Ingrese la cantidad de alumnos: "))

# Bucle para ingresar los datos de cada alumno
for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    
    # Ingreso de las calificaciones
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {i + 1} para {nombre}: "))
                if 0 <= nota <= 20:  # Suponiendo que las notas son de 0 a 20
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20. Intente nuevamente.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    # Agregar el alumno con sus notas al listado
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)

# Mostrar el listado completo de alumnos
print("\nListado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
