def celsius (cel):  
    return (9 / 5 * cel) + 32
def fahrenheit (fahr):
    return (fahr - 32 ) * 5 / 9

print ("1 Сelsius to fahrenheit \n2 to fahrenheit to celsius:")
choice_translation = input("Select an action: ")

match choice_translation:
    case "1":
        cel = float(input())
        fahr = celsius (cel)
        print ("Fahrenheit:", fahr)
    case "2":
        fahr = float(input())
        cel = fahrenheit (fahr)
        print ("Celsius:", cel)