def fahrenheit_to_celsius(fahrenheit:float)-> float:
  return( fahrenheit - 32 ) * 5/9

from foundations.week1.conversions import fahrenheit_to_celsius

while True: 
  user_input = input('enter temperature in fahrenheit')
  try:
    fahrenheit = float(user_input)
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("celsius:", round(celsius,2))
    break
  except ValueError:
    print('Invalid input please enter a number')