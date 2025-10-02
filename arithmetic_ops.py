a = 18
b = 5

print('\n')

# Addition
print('Addition: ', a + b)

# Subtraction
print('Subtraction: ', a - b)

# Division
print('Division: ', a / b)

# Multiplication
print('Multiplication: ', a * b)

# Integer division (floor division)
print('Integer division: ', a // b)

# Exponentiation
print('Exponentiation: ', a ** b)

# Modulo (remainder)
print('Modulo: ', a % b)


counter = 1 
counter += 1 # 2
counter -= 1 # 1
counter *= 10 # 10
counter /= 1 # 10.0 It returns floating numbers
counter %= 6 # 4.0
counter **= 2 #16.0
counter //= 1.5 #10.0

print(counter)


# -------- PEMDAS -------- 
# Paréntesis
# Exponenciación
# Matemáticas
# División
# Adición
# Sustracción

operation_1 = 2 + 3 * 4
operation_2 = (2 + 3) * 4
operation_3 = (2 + 3) * (4**2) / 8 - 1

print(operation_1)
print(operation_2)
print(operation_3)

# -------- Booleans -------- 
a = 10
b = 10.0 #En Python en cuanto a numeros se detecta que es igual
         # aunque el tipo de dato sea diferente int === float
print(a > b) 
print(a < b) 
print(a >= b) # int === float
print(a <= b) # int === float
print(10 == 3) 
print(10 != 3)