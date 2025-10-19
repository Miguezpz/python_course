#Create a currency.py program that asks 
# the user for the amount they have in pesos, soles, 
# and reais and calculates the total in USD.

# Write code below 💖


def calculate_dollars_leftover():
  colombian_pesos = int(input('How many Colombian pesos are left? '))
  peruvian_soles = int(input('How many Peruvian soles are left? '))
  brazilian_reais = int(input('How many brazilian_reais are left? '))

  colombian_pesos_in_dollars = colombian_pesos * 0.00026
  peruvian_soles_in_dollars = peruvian_soles * 0.29
  brazilian_reais_in_dollars = brazilian_reais * 0.19

  total_leftover_in_dollars = colombian_pesos_in_dollars + peruvian_soles_in_dollars + brazilian_reais_in_dollars

  print(f''''
    ${colombian_pesos} c. pesos = ${colombian_pesos_in_dollars} usd 
    ${peruvian_soles} p. soles = ${peruvian_soles_in_dollars} usd 
    ${brazilian_reais} b. reais = ${brazilian_reais_in_dollars} usd

    Total in USD = ${total_leftover_in_dollars:.2f} 
  ''')
 
calculate_dollars_leftover()