def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    
    if '/' in fecha:
        mes, dia, año = fecha.split('/')
    else:
        mes, dia_año = fecha.split(' ', 1)
        dia, año = dia_año.split(',')
    
    mes = meses.get(mes, mes.zfill(2))
    return f"{año.strip()}-{mes}-{dia.zfill(2)}"

# Solicitar al usuario una fecha
entrada_usuario = input("Ingresa una fecha (MM/DD/AAAA o 'Mes día, AAAA'): ")
resultado = convertir_fecha(entrada_usuario)

print("Fecha en formato AAAA-MM-DD:", resultado)