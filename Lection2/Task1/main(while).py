listik = []
n = int(input("How many items do you want to enter?"))
i = 0

while i < n:
    element = input(f"Enter element {i + 1}: ")
    listik.append(element)
    i += 1

un_elements = set(listik)
print("=======================================")
print("Unique elements:", un_elements)