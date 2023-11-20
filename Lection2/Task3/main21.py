def Dividers_num(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers

def prime_numbers_up_to_n(n):
    prime = []
    for num in range(1, n + 1):
        dividers = Dividers_num(num)
        print(f"{num}: {dividers}")
        if len(dividers) == 2:
            prime.append(num)

    return prime

n = int(input("Enter a natural number n: "))
print("Table of numbers from 1 to", n, "with their divisors:")
prime_numbers = prime_numbers_up_to_n(n)
print("\nПростые числа от 1 до", n, ":", prime_numbers)