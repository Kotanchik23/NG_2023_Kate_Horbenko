symbol = {'letters':0 , 'number':0 , 'Special characters':0}
letter_counter = {}

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
    for symbole in text:
        if symbole in letter_counter:
            letter_counter[symbole] += 1
        else:
            letter_counter[symbole] = 1

print(f"The text contains: {symbol}")
print(f"print: {letter_counter}")
