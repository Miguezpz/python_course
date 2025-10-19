# Create a hypotenuse.py program that asks the user for two numbers, a and b, and 
# then calculates the hypotenuse c

# Write code below 💖

def calculate_hypotenuse():
  
  side_a = int(input('What\'s the size for A side in cm? '))
  side_b = int(input('What\'s the size for B side in cm? '))
  hypotenuse = ((side_a ** 2) + (side_b ** 2)) ** 0.5
  return hypotenuse

hypotenuse_size = calculate_hypotenuse()

print(f'Hypotenuse size is = {hypotenuse_size:.2f} cm')