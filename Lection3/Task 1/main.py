symbol = {'letters':0 , 'number':0 , 'Special characters':0}
your_file = input("Enter a file name:")

with open(your_file, "r") as file:
    text = file.read()
    for symbols in text:
        if symbols.isalpha():
            symbol['letters'] += 1
        elif symbols.isdigit():
            symbol['number'] += 1
        else:
            symbol['Special characters'] += 1

print(f"The text contains: {symbol}")