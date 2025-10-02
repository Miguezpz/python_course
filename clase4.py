# ================================
# Python Strings Summary
# ================================

value_1 = 'Hello'
__value1__ = 'value'  
# ⚠️ Not recommended for normal variables.
# Names with double underscores __like_this__ are "special" in Python
# and are reserved for internal use (dunder methods).

# ----------------
# String functions
# ----------------
print(len(value_1))        # returns the string length → 5
print(value_1.strip())     # removes leading/trailing spaces
print(value_1.lower())     # converts to lowercase → 'hello'
print(value_1.upper())     # converts to uppercase → 'HELLO'

# ----------------
# String indexing
# ----------------
print(value_1[0])          # first character → 'H'
print(value_1[-1])         # last character → 'o'

# ----------------
# String repetition
# ----------------
print(5 * value_1)  
# prints 'HelloHelloHelloHelloHello'

# ----------------
# Why __value__ ?
# ----------------
# Double underscores at the start and end (__name__) are used by Python
# for special methods, not for normal variables.
# Examples:
#   __init__  → class constructor
#   __str__   → string representation of an object
#   __len__   → behavior of len(object)

# ✅ For normal variables, use standard names:
my_value = "Hello"
_private_value = "Secret"  # "_" prefix = convention for "private"

# Triple quotes allow multiline strings
triple_comilla = '''Miguel


Madrigal'''
print(triple_comilla)

name = "MIGUEL Jonathan"
last_name = " Madrigal González "

print(5 * name)
print(name + " " + last_name)

# Good practices: 
# Use consistent single or double quotes

print(len(name))
print(len(last_name))
print(name.lower())
print(name.upper())
# Removes spaces at beginning and end
print(last_name.strip()) 
print(name[1], name[2])

# ========================
# String manipulations
# ========================
next_date = "September 23"
print(next_date.upper())
print(next_date.lower())
print("Length:", len(next_date))

# ========================
# Type conversions
# ========================
number = 2
print(type(number))   # int

number = str(number)
print(type(number))   # str

number = int(number)
print(type(number))   # int

number = bool(1)
print(type(number), number)  # bool True

print(float(number))  # 1.0
