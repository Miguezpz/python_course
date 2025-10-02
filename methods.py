# ================================
# exec() - Ejecutar código dinámico
# ================================
sub_code = '''
def greet(name):
    print(f'Hello, mr. {name}')
'''

# Con exec(), el string se interpreta como código Python
exec(sub_code)

# Ahora greet() existe en el contexto actual
greet("Miguel")   # 👉 Output: Hello, mr. Miguel #type: ignore

 
# ================================
# eval() - Evaluar expresiones
# ================================
expression = '2 * 2'
print(eval(expression))   # 👉 Output: 4
# ⚠️ eval() ejecuta expresiones dentro de un string.
# ¡Peligroso si el string viene de usuarios externos!


# ================================
# f-strings - Interpolación de variables
# ================================
user_name = 'Miguel'
string_one = f'Hello mr. {user_name}'
print(string_one)   # 👉 Output: Hello mr. Miguel

# f-strings permiten insertar variables o expresiones dentro de { }
age = 30
print(f"{user_name} is {age} years old.")   # 👉 Output: Miguel is 30 years old
