# Pide el nombre del usuario
nombre_usuario = input("¿Cuál es tu nombre? ")

# Convierte el nombre de usuario a mayúsculas
nombre_usuario_mayusculas = nombre_usuario.upper()

# Cuenta el número de letras del nombre de usuario
numero_letras = len(nombre_usuario_mayusculas)

# Imprime el nombre de usuario y el número de letras
print(f"{nombre_usuario_mayusculas} tiene {numero_letras} letras.")
