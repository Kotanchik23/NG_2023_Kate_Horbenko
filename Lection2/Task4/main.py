word = input("Enter a word: ")
list = []
letters = ("a","е","є","и","і","ї","о","у","я","ю")

for i in word:
    if i in letters:
        list.append(i)

print(list)