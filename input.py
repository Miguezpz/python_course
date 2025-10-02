name = input('Enter you name: ')
print(name)

age = input('Enter your age: ')
print(age)

print(f''''

    \n name: {type(name)}
    age: {type(age)}

''')

#Even if we enter a number as input, it is
#taken as string

age = int(input('What is your age? '))
print(type(age))



#Investigar que es Casting
#Como reminder, la teacher ingreso un string
#donde se pide un integer en el input
#y dio error