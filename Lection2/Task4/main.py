word = input("Enter a word: ")
list = []
letters = ("а","е","є","и","і","ї","о","у","я","ю")

for letter in word:
    if letter in letters:
        list.append(letter)

print(list)