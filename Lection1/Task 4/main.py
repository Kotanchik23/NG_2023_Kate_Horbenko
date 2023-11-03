def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Division by zero is impossible"
    return x / y
def square_root(x):
    if x < 0:
        return "You can't take the root of a negative number"
    return x ** (1 / y)
def power(x, y):
    return x ** y

print("Available operations:\n1. Add (+)\n2. Sub (-)\n3. Mul (*)\n4. Div (/)\n5. Square_root\n6. Power")
ope = input("Select an action: ")

x = float(input("First numb(x): "))
y = float(input("Second numb(y): "))

match ope:
    case "1":
        result = add(x, y)
    case "2":
        result = sub(x, y)
    case "3":
        result = mul(x, y)
    case "4":
        result = div(x, y)
    case "5":
        result = square_root(x)
    case "6":
        result = power(x, y)
print(f"Result = {result}")