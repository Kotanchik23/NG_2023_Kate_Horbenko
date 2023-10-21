def unique_elements():
    op = input("How many variables do you want to include in your writing?: ")
    listik = op.split()
    unique_elements_set = set(listik)
    print("Unique elements: ", *unique_elements_set)
unique_elements()
