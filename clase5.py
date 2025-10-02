x = 10
print(type(x))
#INT = Integer = Entero

y = 5.678
print(type(y))
# Float = Punto Flotante


number = 12.4312
fixed_number = round(number, 2)
#fixing floating numbers

#Cuando trabajamos con numeros muy
#grandes se recomienda usar la notación
#científica

z = 1.2E6 #Puedes utilizar e o E
print(z)
# 1e6 represents 1,000,000 and 
# 1e-6 represents 0.000001


a = 1.2E-6
print(a)


print(x + x)
print(x + y)
print(y + y)
is_true = True
is_false = False
print(type(is_true))
#Para booleanos la primera letra debe ser 
#mayuscula

print("hello" == "hello")

#Dato curioso : El nombre de "bool" 
# viene del matemático "George Boole" 
# ya que creo el algebra booleana, 
# un algebra que solo puede ser "True" 
# o "False" y que en la actualidad forma 
# la base de la lógica computacional moderna

print(float(2))
print(int(2.6))
print(int(True))
print(int(False))
print(bool(1))
print(float(True))
print(type("hello" == "world"))

print("Never","stop","learning",sep='+')