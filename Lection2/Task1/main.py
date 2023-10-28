elements = []
while True:
    user_input = input("Введите элемент (или 'q' для завершения): ")
    if user_input.lower() == 'q':
        break
    elements.append(user_input)
unique_elements = set(elements)
print("Уникальные элементы:", unique_elements)
