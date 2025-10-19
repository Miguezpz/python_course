#Create a bmi.py program that calculates your own BMI.

# Write code below 💖

def calculate_bmi():
  
  mass_kg = float(input('What is your weight in kg? '))
  height_mts = float(input('What is your height in mts? '))

  bmi = mass_kg / (height_mts ** 2)

  print(f'''
    My weight102 is: {mass_kg} kilograms
    My height is: {height_mts} meters
    My body mass index is: {bmi:.2f}
  ''')

calculate_bmi()