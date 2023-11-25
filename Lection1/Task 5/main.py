import math

def quadratic_equation(a, b, c):
    dis = b**2 - 4*a*c
    if a == 0:
        return "If a = 0, the equation becomes linear"
    if dis > 0:
        root1 = (-b + dis**0.5) / (2*a)
        root2 = (-b - dis**0.5) / (2*a)
        return root1, root2
    elif dis == 0:
        root = -b / (2*a)
        return root

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))

roots = quadratic_equation(a, b, c)
print("Roots:", roots)