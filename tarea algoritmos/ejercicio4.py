# Pide el número de teléfono
numero_telefono = input("Introduce un número de teléfono: ")

# Obtiene el prefijo, el número y la extensión del número de teléfono
prefijo = numero_telefono[:4]
numero = numero_telefono[5:-3]
extension = numero_telefono[-3:]

# Imprime el número de teléfono sin el prefijo y la extensión
print(f"El número de teléfono sin prefijo y extensión es: {numero}")
