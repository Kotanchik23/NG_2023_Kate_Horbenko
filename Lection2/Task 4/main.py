word = input("Enter a word: ")
list = []
letters = ("a","e","i","o","u","y", "A", "E", "I", "O", "U", "Y")

for letter in word:
    if letter in letters:
        list.append(letter)

print(list)