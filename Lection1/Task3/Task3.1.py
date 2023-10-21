print("1 Сelsius to fahrenheit \n2 to fahrenheit to celsius:")
vub=int(input())
def fupit(cel):
  return (9/5 * cel) +32
def furit(fahr):
  return (fahr-32)*5/9
if vub==1:
   cel= float(input())
   fahr= fupit(cel)
   print("Fahrenheit:", fahr)
if vub==2:
    fahr= float(input())
    cel= furit(fahr)
    print("Celsius:", cel)