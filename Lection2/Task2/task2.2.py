def unique_elements():
    op = input("Add the variables you want in your letter?: ")
    listik = op.split()
    unique_elements_set = set(listik)
    unique_elements_set = int()
    print("Unique elements: ", *unique_elements_set)
unique_elements()