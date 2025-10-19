# ============================================
# 🐍 RESUMEN DE ESTUDIO - LISTAS EN PYTHON
# ============================================

# Crear una lista simple con tareas
to_do = [
    'Dirigirnos al hotel',
    'Ir a almorzar',
    'Visitar un museo',
    'Volver al hotel'
]

print(to_do)  # Muestra la lista completa


# ============================================
# Tipos de listas y mezcla de tipos
# ============================================

numbers = [1, 2, 3, 4, 'cinco']
print(type(numbers))  # <class 'list'>

# Lista con mezcla de tipos de datos
mix = [
    'uno',      # str
    2,          # int
    3.14,       # float
    True,       # bool
    [1, 2, 3]   # lista anidada
]

print(mix)
print(len(mix))  # Longitud de la lista


# ============================================
# Acceder a elementos individuales
# ============================================

print('Primer elemento: ', mix[0])
print('Segundo elemento: ', mix[1])
print('Tercer elemento: ', mix[2])
print('Cuarto elemento: ', mix[3])
print('Quinto elemento: ', mix[4])

# Índices negativos: cuentan desde el final
print('Último elemento: ', mix[-1])


# ============================================
# SLICING (Rebanado de listas y cadenas)
# ============================================

string = 'Hola mundo'

# Acceder a caracteres individuales
print('Primer elemento: ', string[0])
print('Segundo elemento: ', string[1])
print('Tercer elemento: ', string[2])
print('Cuarto elemento: ', string[3])
print('Quinto elemento: ', string[4])
print('Último elemento: ', string[-1])

# Ejemplos de slicing en listas
print(mix[1:3])   # Elementos desde índice 1 hasta antes del 3
print(mix[0:2])   # Desde índice 0 hasta antes del 2
print(mix[:2])    # Omite el 0 (inicio por defecto)
print(mix[2:-2])  # Desde índice 2 hasta el antepenúltimo


# ============================================
# MÉTODOS DE LISTAS
# ============================================

print('\nLista original:', mix)

# .append() → Agrega al final de la lista
mix.append(False)
print('Después de append(False):', mix)

# .append() también puede agregar otra lista completa
mix.append(['a', 'b'])
print('Después de append([\'a\', \'b\']):', mix)

# .insert() → Inserta en una posición específica
mix.insert(1, ['a', 'b'])
print('Después de insert(1, [\'a\', \'b\']):', mix)

# .index() → Devuelve el índice de la primera coincidencia
print(f"\nÍndice de ['a', 'b']: {mix.index(['a', 'b'])}")


# ============================================
# max() y min() en listas numéricas
# ============================================

numbers = [1, 2, 100.01, 90, 45, 3, 4, 5]

print(f'\nLista: {numbers}')
print('Valor máximo:', max(numbers))
print('Valor mínimo:', min(numbers))


# ============================================
# ELIMINAR ELEMENTOS DE UNA LISTA
# ============================================

# Eliminar el último elemento
del numbers[-1]
print('Después de eliminar el último elemento:', numbers)

# Eliminar los dos primeros elementos
del numbers[:2]
print('Después de eliminar los dos primeros elementos:', numbers)

# Eliminar la lista completa
del numbers

# Esta línea generará un error si se ejecuta,
# porque la lista 'numbers' ya no existe
# print(numbers)
