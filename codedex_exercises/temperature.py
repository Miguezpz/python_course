#Create a temperature.py program that converts a number
#from Fahrenheit (°F) to Celsius (°C).

# Write code below 💖

def calculate_celsius_temperature(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) / 1.8
    return celsius_temp



fahrenheit_temp = 204.4395
celsius_temp = calculate_celsius_temperature(fahrenheit_temp)

print(f'{fahrenheit_temp} degrees fahrenhit is equal to {celsius_temp:.2f} degrees celsius')

