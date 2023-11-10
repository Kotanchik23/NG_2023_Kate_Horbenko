listik = []
n = int(input("How many items do you want to enter?"))

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    listik.append(element)

un_elements = set(listik)
print("=======================================")
print("Unique elements:", un_elements)