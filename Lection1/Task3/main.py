print("1 Сelsius to fahrenheit \n2 to fahrenheit to celsius:")
choice_translation = int(input())
def celsius (cel):
  return (9/5 * cel) + 32
def fahrenheit (fahr):
  return (fahr - 32) * 5/9
if choice_translation == 1:
  cel = float(input())
  fahr= celsius(cel)
  print("Fahrenheit:", fahr)
if choice_translation == 2:
  fahr = float(input())
  cel = fahrenheit(fahr)
  print("Celsius:", cel)