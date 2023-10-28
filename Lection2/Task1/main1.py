listik = []
while True:
    your_elements = input("Введите элемент (или 'end' для завершения): ")
    if your_elements.lower() == 'end':
        break
unique_elements_set = set(listik)
print("Unique elements: ", *unique_elements_set)

