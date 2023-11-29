def Dividers_num(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers

def prime_numbers_up_to_n(natural_num):
    prime = []
    for num in range(1, natural_num + 1):
        dividers = Dividers_num(num)
        print(f"{num}: {dividers}")
        if len(dividers) == 2:
            prime.append(num)

    return prime

natural_num = int(input("Enter a natural number n: "))
print("Table of numbers from 1 to", natural_num, "with their divisors:")
prime_numbers = prime_numbers_up_to_n(natural_num)
print("\nSimple numbers from 1 to", natural_num, ":", prime_numbers)