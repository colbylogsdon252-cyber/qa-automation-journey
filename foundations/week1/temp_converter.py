while True: 
  fahrenheit = input('enter temperature in fahrenheit')
  try:
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * 5/9
    print("celsius:", round(celsius,2))
    break
  except ValueError:
    print('Invalid input please enter a number')