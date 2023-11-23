numb = input("Enter a set of elements: ").split()
list = []

for element in numb:
    try:
        elements = float(element)
        list.append(elements)
    except ValueError:
        pass

if list:
    print("The following elements are numbers:",list, "\nThe number of elements:", len(list))
else:
    print("There are no numbers in your set. ")
