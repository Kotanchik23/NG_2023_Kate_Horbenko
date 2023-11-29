def celsius (cel):  
    return (9 / 5 * cel) + 32
def fahrenheit (fahr):
    return (fahr - 32 ) * 5 / 9

print ("1 Сelsius to fahrenheit \n2 to fahrenheit to celsius:")
choice_translation = input("Select an action: ")
num = float(input("Enter number:"))

match choice_translation:
    case "1":
        #cel = float(input("Enter celsius: "))
        fahr = celsius (num)
        print ("Fahrenheit:", fahr)
    case "2":
        #fahr = float(input("Enter fahrenheit: "))
        cel = fahrenheit (num)
        print ("Celsius:", cel)
        
