def prime_num (num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def table (n):
    table = []
    for i in range(1, n + 1):
        divisor = [j for j in range(1, i + 1) if i % j ==0 ]
        table.append((i, divisor))
        return table


def prime (num):
    primes = []
    for num in range(1, num + 1):
        if prime(num):
            primes.append(num)
            
print("ТNumbers\t| divisor")
print("======================")

for num, divisors in table:
    print(f"{num}\t| {divisors}")

    print("\nПростые числа:")
    print(num)

user_input = int(input("Введите число: "))
table(user_input)