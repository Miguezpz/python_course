# ==============================
#   Resumen sobre print en Python
# ==============================

# Valores de ejemplo
username = 'Garfio'
island = 'Hawaii'

# ------------------------------
# sep → separador entre valores
# ------------------------------
print(username, island, sep=' || ')

# ------------------------------
# end → valor por defecto es '\n'
# ------------------------------
print(username, end=' -> \n')
print(island, end=' -> \n')

# ------------------------------
# f-strings → interpolación moderna
# ------------------------------
print(f'username: {username}', f'island: {island}', sep='\n')

# ------------------------------
# .format() → forma más antigua
# ------------------------------
# Ejemplo 1
print('username: {}, island: {}'.format(username, island))

# Ejemplo 2
valor1 = 'Abra'
valor2 = 'Cadabra'
print('{}, {}'.format(valor1, valor2))

# ------------------------------
# .format() con floats
# ------------------------------
valor = 3.14159
print("Valor: {:.2f}".format(valor))  # :.2f → dos decimales

favorite_number = 7.7777777
print('{:.3f}'.format(favorite_number))  # format con 3 decimales
print(f'{favorite_number:.4f}')          # f-string con 4 decimales


pi=3.14159
print(f"El valor de pi es {pi:.2f}") #output: El valor de pi es 3.14


# ------------------------------
# Saltos de línea con \n
# ------------------------------
print('Hola\nmy\nfriend')

# ------------------------------
# Uso de comillas dentro de strings
# ------------------------------
# Ejemplo con error:
# print('Hello my name is 'Charles'')  # ❌ genera error de sintaxis

# Forma correcta escapando comillas:
print('Hello my name is \'Charles\'')

# ------------------------------
# Uso de \ en rutas de archivos
# ------------------------------
# Ejemplo con error:
# print('La ruta es: C:\Users\Usuario\Desktop\archivo.txt')  # ❌ error por \U

# Forma correcta: escapar cada \ "backslash" o "carácter de escape"
print('La ruta es: C:\\Users\\Usuario\\Desktop\\archivo.txt')

# Alternativa: usar raw string (r'...')
print(r'La ruta es: C:\Users\Usuario\Desktop\archivo.txt')


# ------------------------------
# Backslash (\)
# ------------------------------

# 1) Usar backslash para continuar una línea de código (poco usado hoy en día)
suma = 1 + 2 + 3 + \
       4 + 5 + 6
print(suma)  # 21

# 2) Aunque se prefiere usar paréntesis para dividir líneas largas:
suma = (1 + 2 + 3 +
        4 + 5 + 6)
print(suma)  # 21

